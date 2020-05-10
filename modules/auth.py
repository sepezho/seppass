from os import system
from json import loads
from gnupg import GPG
from sqlite3 import connect

from settings import settings_begin_mess
from del_mess import del_mess

import threading
result_available = threading.Event()
pas = None


def auth_main(message, bot):
	is_login = '(0,)'

	try:
		conn = connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "SELECT COUNT(*) FROM Users WHERE User_id = 'user_"+str(message.chat.id)+"'"
		c.execute(query)
		is_login = str(c.fetchone())
		conn.commit()
		conn.close()

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return None

	if is_login == '(0,)':
		return settings_begin_mess(message, bot, False, None)

	else:
		return finish_auth(message, bot)


def finish_auth(message, bot):
	try:
		conn = connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "SELECT Settings FROM Users WHERE User_id = 'user_"+str(message.chat.id)+"'"
		res = c.execute(query).fetchall()[0][0]
		res = res.replace("'", '"')
		res_parse = loads(res)
		conn.commit()
		conn.close()

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return None

	if res_parse["store_pass"] == 'pass_server':
		try:
			with open('/Seppass/Users_folder/user_' + str(message.chat.id) + '/user_data/Nothing.txt', 'r') as f:
				password = f.read()
			msg = bot.send_message(message.chat.id, 'Вы аутентифицировались.')
			del_mess(msg, bot, 2)
			return password

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
			del_mess(msg, bot, 2)
			return None

	else:
		thread = threading.Thread(target=finish_auth_pass_handler(message, bot))
		thread.start()
		result_available.wait()
		return pas

def finish_auth_pass(message, bot):
	t_str = 'test_ur_crappy_password_str'
	decrypt = None

	try:
		gpg = GPG()
		encrypt = gpg.encrypt(t_str, recipients='user_'+str(message.chat.id))
		decrypt = gpg.decrypt(str(encrypt), passphrase=str(message.text))
		system('echo RELOADAGENT | gpg-connect-agent')

	except:
	 	msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
	 	del_mess(msg, bot, 4)
	 	result_available.set()

	if str(decrypt) == t_str:
		global pas
		msg = bot.send_message(message.chat.id, 'Вы аутентифицировались.')
		pas = str(message.text)
		del_mess(msg, bot, 4)
		result_available.set()

	else:
		msg = bot.send_message(message.chat.id, 'Пароль не верен.')
		del_mess(msg, bot, 4)
		result_available.set()


def finish_auth_pass_handler(message, bot):
	msg_handler = bot.send_message(message.chat.id, 'Введите пароль.')
	bot.register_next_step_handler(msg_handler, lambda msg: finish_auth_pass(msg, bot))
