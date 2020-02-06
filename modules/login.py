import os
import gnupg
import sqlite3
from telebot import types
from main import main

def login_pass_query(message, bot_old, settings_old):
	global bot
	global settings
	bot = bot_old
	settings = settings_old
	msg = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	bot.register_next_step_handler(msg, finish_login)
		
def finish_login(message):
	os.mkdir('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id))
	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	input_data = gpg.gen_key_input(
		passphrase=message.text,
		name_real= str(message.from_user.id))
	key = gpg.gen_key(input_data)
	key = key.fingerprint
	data = ((str(message.from_user.id), key, str(settings)))
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "INSERT INTO Users VALUES (?, ?, ?)"
	c.execute(query, data)
	conn.commit()
	conn.close()
	with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'w') as f:
		f.write(message.text)
	if settings["store_pass"] == "pass_serv":
		bot.send_message(message.chat.id, 'Регистрация прошла успешно. Пароль храниться на сервере.\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key))
	else:
		bot.send_message(message.chat.id, 'Регистрация прошла успешно. Запомните пароль, в случае его утери ваш акк не восстановить (пока).\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key))
	main(message, bot)
