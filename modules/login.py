from os import makedirs
from os import system
from gnupg import GPG
from sqlite3 import connect
from telebot import types
from del_mess import del_mess


def login_pass_query(message, bot, settings):
	msg_handler = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	bot.register_next_step_handler(msg_handler, lambda msg: finish_login(msg, bot, settings))


def finish_login(message, bot, settings):
	try:
		makedirs('/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)+'/main')
		makedirs('/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)+'/user_data')
	
	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return

	try:	
		gpg = GPG()
		input_data = gpg.gen_key_input(
			passphrase=message.text,
			name_real='user_'+str(message.from_user.id)
			)
		key = gpg.gen_key(input_data)
		key = key.fingerprint
		system('echo RELOADAGENT | gpg-connect-agent')

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return

	try:
		data = (('user_'+str(message.from_user.id), key, str(settings)))
		conn = connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "INSERT INTO Users VALUES (?, ?, ?)"
		c.execute(query, data)
		conn.commit()
		conn.close()

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return

	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')

	if settings["store_pass"] == "pass_serv":
		try:
			with open('/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id) + '/user_data/Nothing.txt', 'w') as f:
				f.write(message.text)
		
		except TypeError as e:
			msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
			del_mess(msg, bot, 2)
			return

		msg_handler = bot.send_message(message.chat.id, 'Регистрация прошла успешно. Пароль храниться на сервере.\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key)+'\n\nЗапомнили? Я сейчас это сообщение удалю, в целях сохранности ваших данных.', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: complete_finish_login(msg, bot))

	else:
		msg_handler = bot.send_message(message.chat.id, 'Регистрация прошла успешно. Запомните пароль, в случае его утери ваш акк не восстановить (пока).\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key)+'\n\nЗапомнили? Я сейчас это сообщение удалю, в целях сохранности ваших данных.', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: complete_finish_login(msg, bot))


def complete_finish_login(message, bot):
	bot.send_message(message.chat.id, 'На этом мы закончим.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	msg = bot.send_message(message.chat.id, 'Используйте /auth, чтобы войти.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	del_mess(msg, bot, 5)
	return
