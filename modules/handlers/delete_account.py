import os
import gnupg
import shutil
import sqlite3
from telebot import types


def delete_account_main(message, bot_old, password_old):
	global bot
	global password
	bot = bot_old
	password = password_old
	
	msg_handler = bot.send_message(message.chat.id, 'Вы точно хотите удалить аккаунт? :c \n\nВСЕ ВАШИ ЗАПИСИ БУДУТ БЕЗВОЗВРАТНО УТЕРЯНЫ!!!\n\nЕсли вы уверены, что хотите удалить аккаунт, и уйти от меня, то напишите:\n\nя хoчу удaлить aккaунт')
	bot.register_next_step_handler(msg_handler, delete_account_handler)


def delete_account_handler(message):
	if message.text == 'я хoчу удaлить aккaунт':
		msg_handler = bot.send_message(message.chat.id, 'Не ленитесь, не копируйте текст, а напишите сами.')
		bot.register_next_step_handler(msg_handler, delete_account_handler)
	
	elif message.text == 'я хочу удалить аккаунт':
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Надо.')
		markup.add('Я передумал.')
	
		msg_handler = bot.send_message(message.chat.id, 'ТОЧНО?!?!?!?? Может не надо?(((((', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, delete_account_handler_finish)
	
	else:
		bot.send_message(message.chat.id, 'Вы бредите.')
		return password


def delete_account_handler_finish(message):
	if message.text == 'Надо.':
		bot.send_message(message.chat.id, 'Прощайте!\n\n*звуки смерти*', reply_markup = types.ReplyKeyboardRemove(selective=False))
		rm_db(str(message.from_user.id))
		rm_folder(str(message.from_user.id))
		return None

	elif message.text == 'Я передумал.':
		bot.send_message(message.chat.id, 'Фууух, не пугайте меня так....', reply_markup = types.ReplyKeyboardRemove(selective=False))
		return password

	else:
		bot.send_message(message.chat.id, 'Вы бредите.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		return password
	

def rm_key(key):
	print(key)
	print(str(key))
	gpg = gnupg.GPG()
	gpg.delete_keys(key, True, passphrase=password)
	gpg.delete_keys(key)
	os.system('echo RELOADAGENT | gpg-connect-agent')


def rm_db(user_id):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT Key FROM Users WHERE User_id = 'user_"+str(user_id)+"'"
	key = c.execute(query).fetchall()[0][0]
	rm_key(key)
	query = "DELETE FROM Users WHERE User_id = 'user_"+str(user_id)+"'"
	c.execute(query)
	conn.commit()
	conn.close()


def rm_folder(user_id):
	folder = '/home/sepezho/Documents/seppass/Users_folder/user_' + user_id
	shutil.rmtree(folder)
