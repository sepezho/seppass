import os
import json
import gnupg
import sqlite3
from settings import settings_begin_mess
from del_mess import del_mess

import threading
result_available = threading.Event()
pas = None


def auth_main(message, bot_old):
	global bot
	bot = bot_old
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE User_id = 'user_"+str(message.from_user.id)+"'"
	c.execute(query)
	conn.commit()
	conn.close()

	if c.fetchone() == (0,):
		settings_begin_mess(message, bot, False, None)
	else:
		return finish_auth(message)


def finish_auth(message):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT Settings FROM Users WHERE User_id = 'user_"+str(message.from_user.id)+"'"
	res = c.execute(query).fetchall()[0][0]
	res = res.replace("'", '"')
	res_parse = json.loads(res)
	conn.commit()
	conn.close()
	
	if res_parse["store_pass"] == 'pass_server':
		with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'r') as f:
			password = f.read()
		
		msg = bot.send_message(message.chat.id, 'Вы аутентифицировались.')
		del_mess(msg, bot, 2)
		return password
	
	else:
		thread = threading.Thread(target=finish_auth_pass_handler(message))
		thread.start()
		result_available.wait()
		return pas


def finish_auth_pass_handler(message):
	def finish_auth_pass(message):
		t_str = 'test_str'
		
		try:
			gpg = gnupg.GPG()
			encrypt = gpg.encrypt(t_str, recipients='user_'+str(message.from_user.id))
			decrypt = gpg.decrypt(str(encrypt), passphrase=str(message.text))
		
		except TypeError as e:
			msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
			result_available.set()
		
		if str(decrypt) == t_str:
			os.system('echo RELOADAGENT | gpg-connect-agent')
			msg = bot.send_message(message.chat.id, 'Вы аутентифицировались.')
			global pas
			pas = str(message.text)
			result_available.set()
		
		else:
		 	msg = bot.send_message(message.chat.id, 'Пароль не верен.')
		 	result_available.set()
		
		del_mess(msg, bot, 4)
	
	msg = bot.send_message(message.chat.id, 'Введите пароль.')
	bot.register_next_step_handler(msg, finish_auth_pass)
