import sqlite3
import json
import sys

sys.path.append('./modules/handlers')
from touch import touch_main
from mkd import mkd_main
from cat import cat_main
from ls import ls_main
from rm import rm_main

def main(message, bot_old):
	global bot
	bot = bot_old

	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT Settings FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
	res = c.execute(query).fetchall()[0][0]
	res = res.replace("'", '"')
	res_parse = json.loads(res)
	
	global password
	with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'r') as f:
		password = f.read()
	
	if res_parse["store_pass"] == 'pass_server':
		main_handlers(message)
	else:
		msg = bot.send_message(message.chat.id, 'Введите пароль.')
		bot.register_next_step_handler(msg, sign_response)

def sign_response(message):
	if password == message.text:
		main_handlers(message)
	else:
		msg = bot.send_message(message.chat.id, 'Пароль не верен, повторите ввод.')
		bot.register_next_step_handler(msg, sign_response)

def main_handlers(message):
	bot.send_message(message.chat.id, 'Вы подтвердили что это вы.')
	@bot.message_handler(commands=['touch'])
	def touch_func_in_main(message):
		touch_main(message, bot)
	@bot.message_handler(commands=['mkd'])
	def mkd_handler_auth_main(message):
		mkd_main(message, bot)
	@bot.message_handler(commands=['cat'])
	def cat_func_in_main(message):
		cat_main(message, bot, password)
	@bot.message_handler(commands=['ls'])
	def ls_func_in_main(message):
		ls_main(message, bot)
	@bot.message_handler(commands=['rm'])
	def rm_func_in_main(message):
		rm_main(message, bot)

	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def error(message):
		# if message.text[0] != '/':
		bot.send_message(message.chat.id,'Я смотрю ты потерялся. Используй /help.')
	# @bot.message_handler(commands=['generate'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['edit'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['mv'])
	# def message_handler_auth_main(message):
	# @bot.message_handler(commands=['settings'])
	# def message_handler_auth_main(message):
