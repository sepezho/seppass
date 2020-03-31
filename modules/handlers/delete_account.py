from os import system
from gnupg import GPG
from shutil import rmtree
from sqlite3 import connect
from telebot import types
from del_mess import del_mess


def delete_account_main(message, bot, password):
	msg_handler = bot.send_message(message.chat.id, 'Вы точно хотите удалить аккаунт? :c \n\nВСЕ ВАШИ ЗАПИСИ БУДУТ БЕЗВОЗВРАТНО УТЕРЯНЫ!!!\n\nЕсли вы уверены, что хотите удалить аккаунт, и уйти от меня, то напишите:\n\nя хoчу удaлить aккaунт')
	bot.register_next_step_handler(msg_handler, lambda msg: delete_account_handler(msg, bot, password))


def delete_account_handler(message, bot, password):
	if message.text == 'я хoчу удaлить aккaунт':
		msg_handler = bot.send_message(message.chat.id, 'Не ленитесь, не копируйте текст, а напишите сами.')
		bot.register_next_step_handler(msg_handler, lambda msg: delete_account_handler(msg, bot, password))
	
	elif message.text == 'я хочу удалить аккаунт':
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Надо.')
		markup.add('Я передумал.')
	
		msg_handler = bot.send_message(message.chat.id, 'ТОЧНО?!?!?!?? Может не надо?(((((', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: delete_account_handler_finish(msg, bot, password))
	
	else:
		msg = bot.send_message(message.chat.id, 'Вы бредите.')
		del_mess(msg, bot, 4)
		return password


def delete_account_handler_finish(message, bot, password):
	if message.text == 'Надо.':
		try:
			rm_db(str(message.from_user.id), password)
			rm_folder(str(message.from_user.id))
			msg = bot.send_message(message.chat.id, 'Прощайте!\n\n*звуки смерти*', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 6)
			return None

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
			del_mess(msg, bot, 6)
			return None

	elif message.text == 'Я передумал.':
		msg = bot.send_message(message.chat.id, 'Фууух, не пугайте меня так....', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 6)
		return password

	else:
		msg = bot.send_message(message.chat.id, 'Вы бредите.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 6)
		return password
	

def rm_key(key, password):
	gpg = GPG()
	gpg.delete_keys(key, True, passphrase=password)
	gpg.delete_keys(key)
	system('echo RELOADAGENT | gpg-connect-agent')


def rm_db(user_id, password):
	conn = connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT Key FROM Users WHERE User_id = 'user_"+str(user_id)+"'"
	key = c.execute(query).fetchall()[0][0]
	rm_key(key, password)
	query = "DELETE FROM Users WHERE User_id = 'user_"+str(user_id)+"'"
	c.execute(query)
	conn.commit()
	conn.close()


def rm_folder(user_id):
	folder = '/home/sepezho/Documents/Seppass/Users_folder/user_' + user_id
	rmtree(folder)
