from os import makedirs
from os import system
from os import path
import sys
sys.path.append('./modules/third_party')
from gnupg import GPG
from sqlite3 import connect
from telebot import types
from del_mess import del_mess


def login_pass_query(message, bot, settings):
	msg_handler = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	bot.register_next_step_handler(msg_handler, lambda msg: finish_login(msg, bot, settings))


def finish_login(message, bot, settings):
	user_root_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)
	try:
		if not path.isdir(user_root_folder+'/main'):
			makedirs(user_root_folder+'/main')
		if not path.isdir(user_root_folder+'/user_data'):
			makedirs(user_root_folder+'/user_data')
	
	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
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

		ascii_armored_private_keys = gpg.export_keys(key, True, passphrase=message.text)
		with open(user_root_folder+'/user_data/gpg_private_key.asc', 'w') as f:
			f.write(ascii_armored_private_keys)
		with open(user_root_folder+'/main/gpg_private_key.asc', 'w') as f:
			f.write(ascii_armored_private_keys)

		system('echo RELOADAGENT | gpg-connect-agent')

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
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

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return

	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')

	if settings["store_pass"] == "pass_server":
		try:
			with open(user_root_folder+'/user_data/Nothing.txt', 'w') as f:
				f.write(message.text)
		
		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
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
