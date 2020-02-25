import os
import gnupg
import sqlite3
from telebot import types
from auth import finish_auth
from telebot import types
from del_mess import del_mess



def login_pass_query(message, bot_old, settings_old):
	global bot
	global settings
	bot = bot_old
	settings = settings_old

	msg = bot.send_message(message.chat.id, 'Придумайте пароль.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	bot.register_next_step_handler(msg, finish_login)


def finish_login(message):
	os.mkdir('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id))

	gpg = gnupg.GPG()
	input_data = gpg.gen_key_input(
		passphrase=message.text,
		name_real='user_'+str(message.from_user.id))
	key = gpg.gen_key(input_data)
	key = key.fingerprint
	os.system('echo RELOADAGENT | gpg-connect-agent')

	data = (('user_'+str(message.from_user.id), key, str(settings)))
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "INSERT INTO Users VALUES (?, ?, ?)"
	c.execute(query, data)
	conn.commit()
	conn.close()

	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')

	if settings["store_pass"] == "pass_serv":
		with open('/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) + '/Nothing.txt', 'w') as f:
			f.write(message.text)

		msg_handler = bot.send_message(message.chat.id, 'Регистрация прошла успешно. Пароль храниться на сервере.\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key)+'\n\nЗапомнили? Я сейчас это сообщение удалю, в целях сохранности ваших данных.', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, complete_finish_login)

	else:
		msg_handler = bot.send_message(message.chat.id, 'Регистрация прошла успешно. Запомните пароль, в случае его утери ваш акк не восстановить (пока).\n\nВаш user id:\n'+str(message.from_user.id)+'\n\nПароль:\n'+ message.text +'\n\nЭто ваш отпечаток ключа:\n'+ str(key)+'\n\nЗапомнили? Я сейчас это сообщение удалю, в целях сохранности ваших данных.', reply_markup = markup)
		bot.register_next_step_handler(msg_handler, complete_finish_login)


def complete_finish_login(message):
	msg = bot.send_message(message.chat.id, 'На этом мы закончим.', reply_markup = types.ReplyKeyboardRemove(selective=False))
	del_mess(msg, bot, 4)
	finish_auth(message)
