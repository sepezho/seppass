import sqlite3
import json

from telebot import types
from settings import settings_pre_begin

def start_main(message, bot_old):
	global bot
	bot = bot_old
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Вход', 'Регистрация')
	if message.chat.username:
		msg = bot.send_message(message.chat.id, 'Привет, '+message.chat.username+' !\nТы новенький или уже имел со мной дело?', reply_markup=markup)
	elif message.chat.first_name:
		msg = bot.send_message(message.chat.id, 'Привет, '+message.chat.first_name+' !\nТы новенький или уже имел со мной дело?', reply_markup=markup)
	else:
		msg = bot.send_message(message.chat.id, 'Привет!\nТы новенький или уже имел со мной дело?', reply_markup=markup)

	bot.register_next_step_handler(msg, start_handling)

def start_handling(message):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
	c.execute(query)

	if c.fetchone() == (0,):
		settings_pre_begin(message, bot)
	else:
		query = "SELECT Settings FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
		res = c.execute(query).fetchall()[0][0]
		res = res.replace("'", '"')
		res_parse = json.loads(res)
		print(res_parse["store_pass"])
		# bot.send_message(message.chat.id, 'Ваш телеграм уже связан с вашим акк для этого бота.\n\nВойдите в акк, отправив снова /start', reply_markup = types.ReplyKeyboardRemove(selective=False))

	conn.commit()
	conn.close()


def start_response(message):
	if message.text == 'Вход':
		sign_begin(message)
	elif message.text == 'Регистрация':
		login_begin(message)
	else:
		bot.send_message(message.chat.id, 'Непонел.', reply_markup = types.ReplyKeyboardRemove(selective=False))

def login_begin(message):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
	c.execute(query)
	answer = c.fetchone()
	conn.commit()
	conn.close()

	if answer == (0,):
		settings_pre_begin(message, bot)
	else:
		bot.send_message(message.chat.id, 'Ваш телеграм уже связан с вашим акк для этого бота.\n\nВойдите в акк, отправив снова /start', reply_markup = types.ReplyKeyboardRemove(selective=False))

def sign_begin(message):
	bot.send_message(message.chat.id, 'Вход пожилой!', reply_markup = types.ReplyKeyboardRemove(selective=False))


class JSON2dict(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)