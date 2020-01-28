import os
import sqlite3

from telebot import types
from cryptography.fernet import Fernet

def start_main(message, bot_old):
	global bot
	bot = bot_old
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Вход', 'Регистрация')
	msg = bot.send_message(message.chat.id, 'Привет, '+message.chat.username+' !\nТы новенький или уже имел со мной дело?', reply_markup=markup)
	bot.register_next_step_handler(msg, start_response)

def start_response(message):
	if message.text == 'Вход':
		sign(message)
	elif message.text == 'Регистрация':
		login(message)
	else:

		bot.send_message(message.chat.id, 'Непонел.', reply_markup = types.ReplyKeyboardRemove(selective=False))

def login(message):

	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE Username = '" + message.chat.username + "'"
	answer = c.execute(query)
	conn.commit()
	conn.close()

	if answer != 0:
		msg = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		bot.register_next_step_handler(msg, login_response)
	else:
		bot.send_message(message.chat.id, 'Ваш телеграм уже связан с вашим акк для этого бота.\n\nВойдите в акк, отправив снова /start', reply_markup = types.ReplyKeyboardRemove(selective=False))
		return

def login_response(message):
	cipher_key = Fernet.generate_key()
	cipher = Fernet(cipher_key)

	# passw = message.text.decode("utf-8")
	passw_ascii=message.text.encode("utf-8")

	encrypted_pass = cipher.encrypt(passw_ascii)

	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "INSERT INTO Users (Username, Password, Settings) VALUES ('"+ message.chat.username +"', '"+encrypted_pass.decode('utf-8"')+"', 'obj')"
	c.execute(query)
	conn.commit()
	conn.close()

	# os.mkdir('/home/sepezho/Documents/teleBot_seppass/Users_folders/' + message.chat.username)

	bot.send_message(message.chat.id, 'Пароль зашифрован и сохранен в БД. Так же создана папка, где ваш никнейм выступил в качестве названия.\n\nПароль:\n'+ encrypted_pass.decode('utf-8"')+'\n\nЭто ваш крипто-ключ:\n'+ cipher_key.decode('utf-8"') + '\n\nСохраните его где-нибудь.')

def sign(message):
	bot.send_message(message.chat.id, 'Вход пожилой!', reply_markup = types.ReplyKeyboardRemove(selective=False))
