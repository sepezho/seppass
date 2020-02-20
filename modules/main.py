import sqlite3
import json
import sys
import gnupg
import os

sys.path.append('./modules/handlers')
from touch import touch_main
from mkd import mkd_main
from cat import cat_main
from ls import ls_main
from rm import rm_main
from mv import mv_main
from gen import gen_main
from edit import edit_main
import settings

def main(message, bot_old):
	global bot
	bot = bot_old

	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT Settings FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
	res = c.execute(query).fetchall()[0][0]
	res = res.replace("'", '"')
	res_parse = json.loads(res)

	if res_parse["store_pass"] == 'pass_server':
		with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'r') as f:
			password = f.read()
		main_handlers(message, password)
		return password
	else:
		return False

def func_password_handler()
	msg = bot.send_message(message.chat.id, 'Введите пароль.')
	bot.register_next_step_handler(msg, sign_response)

def sign_response(message):
	t_str = 'test_str'
	try:
		# gpg = gnupg.GPG(gnupghome='/home/sepezho/.gnupg')
		gpg = gnupg.GPG()
		encrypt = gpg.encrypt(t_str, recipients='user_'+str(message.from_user.id))
		decrypt = gpg.decrypt(str(encrypt), passphrase=str(message.text))
	except TypeError as e:
		bot.send_message(message.chat.id, 'Error: '+ str(e))
		return
	if str(decrypt) == t_str:
		os.system('echo RELOADAGENT | gpg-connect-agent')
		main_handlers(message, str(message.text))
		return True
	else:
	 	bot.send_message(message.chat.id, 'Пароль не верен.')
	 	return False

def main_handlers(message, password):
	bot.send_message(message.chat.id, 'Вы аутентифицировались.')

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
	@bot.message_handler(commands=['mv'])
	def mv_handler_auth_main(message):
		mv_main(message, bot)
	@bot.message_handler(commands=['gen'])
	def gen_handler_auth_main(message):
		gen_main(message, bot)
	@bot.message_handler(commands=['edit'])
	def edit_handler_auth_main(message):
		edit_main(message, bot)
	@bot.message_handler(commands=['settings'])
	def settings_handler_auth_main(message):
		settings.settings_begin_mess(message, bot, True, password)

	@bot.message_handler(func=lambda message: True, content_types=['text'])
	def error(message):
		if message.text[0] != '/':
			bot.send_message(message.chat.id,'Я смотрю ты потерялся. Используй /help.')
		else:
			bot.send_message(message.chat.id,'Функции '+message.text+' не существует. Используй /help.')
	