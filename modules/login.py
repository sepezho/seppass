import os
import gnupg
import sqlite3
from telebot import types

def login_response_begin(message, bot_old, settings_old):
	global bot
	global settings
	bot = bot_old
	settings = str(settings_old)
	msg = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	bot.register_next_step_handler(msg, login_response)
		
def login_response(message):

	gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg/')
	input_data = gpg.gen_key_input(
	    passphrase=message.text,
		name_real=message.chat.username)
	key = gpg.gen_key(input_data)
	key = key.fingerprint

	data = ((message.chat.username, key, settings))
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "INSERT INTO Users VALUES (?, ?, ?)"
	c.execute(query, data)
	conn.commit()
	conn.close()

	os.mkdir('/home/sepezho/Documents/seppass/Users_folder/' + message.chat.username)
	bot.send_message(message.chat.id, 'Пароль зашифрован и сохранен в БД. Так же создана папка, где ваш никнейм выступил в качестве названия.\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key))
	# settings_begin(message)
	