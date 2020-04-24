from os import path
from os import system
from git import Git
from git import Repo
from gnupg import GPG
from json import loads
from sqlite3 import connect
from shutil import rmtree
from shutil import copy2
from telebot import types
from del_mess import del_mess
from ls import ls


def git_clone_main(message, bot, password):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)
	text = ls(path_to_user_folder+'/main')
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Нет')
	msg_handler = bot.send_message(message.chat.id, 'Вы действительно хотите удалить все содержимое папки /main, и клонировать репозиторий с gitHub?\n\n'+text, reply_markup = markup)
	bot.register_next_step_handler(msg_handler, lambda msg: git_clone_main_request(msg, bot, path_to_user_folder, password))

def git_clone_main_request(message, bot, path_to_user_folder, password):
	if message.text == 'Да':
		if path.isfile(path_to_user_folder+'/user_data/ssh_key.pub'):
			msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой репозиторий.')
			bot.register_next_step_handler(msg_handler, lambda msg: clone_repo(msg, bot, path_to_user_folder, password))

		else:
			msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи /gitgenssh), и закинте его на свой gitHub.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 4)
			return

	elif message.text == 'Нет':
		msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return

	else:
		msg = bot.send_message(message.chat.id, 'Я вас не понял ._.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return

def clone_repo(message, bot, path_to_user_folder, password):

	try:
		if path.isdir(path_to_user_folder+'/main'):
			rmtree(path_to_user_folder+'/main')
		with open(path_to_user_folder+'/user_data/token.txt', 'r') as f:
			token = f.read()
		with Git().custom_environment(HTTPS_REMOTE_URL='https://'+token+':x-oauth-basic@'+message.text[8:]):
			Repo.clone_from('https://'+token+':x-oauth-basic@'+message.text[8:], path_to_user_folder+'/main')

			if path.isfile(path_to_user_folder+'/main/gpg_private_key.asc'):
				markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
				markup.add('Да')
				markup.add('Нет')
				msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что хотите поменять gpg ключ на тот, который находися в репозитории?', reply_markup = markup)
				bot.register_next_step_handler(msg_handler, lambda msg: db_change_plus_copy(msg, bot, str(message.from_user.id), password, path_to_user_folder))

			else:
				msg = bot.send_message(message.chat.id, 'Я закончил.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				del_mess(msg, bot, 4)
				return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return


def db_change_plus_copy(message, bot, user_id, password, path_to_user_folder):

	if message.text == 'Да':
		conn = connect('DataBase.db', check_same_thread=False)
		c = conn.cursor()
		query = "SELECT Key FROM Users WHERE User_id = 'user_"+user_id+"'"
		key = c.execute(query).fetchall()[0][0]
		query = "SELECT Settings FROM Users WHERE User_id = 'user_"+str(message.from_user.id)+"'"
		res_arr = c.execute(query).fetchall()[0][0]
		res_arr = res_arr.replace("'", '"')
		res_parse = loads(res_arr)
		new_key = key_edit(key, password, path_to_user_folder)
		query = "UPDATE Users SET Key = '"+new_key+"' WHERE User_id = 'user_"+user_id+"'"
		c.execute(query)
		conn.commit()
		conn.close()

		if res_parse["store_pass"] == 'pass_server':
			msg_handler = bot.send_message(message.chat.id, 'Введите пароль от нового ключа, я его сохраню.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			bot.register_next_step_handler(msg_handler, lambda msg: finish_clone_pass(msg, bot, path_to_user_folder))

		else:
			msg = bot.send_message(message.chat.id, 'Я закончил.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 6)
			return

	else:
		msg = bot.send_message(message.chat.id, 'Хорошо, оставлю старый ключ.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 6)
		return


def key_edit(key, password, path_to_user_folder):

	try:
		gpg = GPG()
		gpg.delete_keys(key, True, passphrase=password)
		gpg.delete_keys(key)
		key_data = open(path_to_user_folder+'/main/gpg_private_key.asc').read()
		new_key = gpg.import_keys(key_data)
		new_key = new_key.results[0]['fingerprint']
		gpg.trust_keys(new_key, "TRUST_ULTIMATE")
		system('echo RELOADAGENT | gpg-connect-agent')
		copy2(path_to_user_folder+'/main/gpg_private_key.asc', path_to_user_folder+'/user_data/gpg_private_key.asc')
		return new_key

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 6)
		return key


def finish_clone_pass(message, bot, path_to_user_folder):

	t_str = 'test_ur_crappy_password_str'
	decrypt = None

	try:
		gpg = GPG()
		encrypt = gpg.encrypt(t_str, recipients='user_'+str(message.from_user.id))
		decrypt = gpg.decrypt(str(encrypt), passphrase=message.text)
		system('echo RELOADAGENT | gpg-connect-agent')

	except:
	 	msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
	 	del_mess(msg, bot, 8)
	 	return

	if str(decrypt) == t_str:
		try:
			with open(path_to_user_folder+'/user_data/Nothing.txt', 'w') as f:
				f.write(message.text)
			msg = bot.send_message(message.chat.id, 'Пароль сохранен.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 8)
			return

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 8)
			return

	else:
		msg = bot.send_message(message.chat.id, 'Пароль не верен.')
		msg_handler = bot.send_message(message.chat.id, 'Введите пароль от нового ключа, я его сохраню.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		bot.register_next_step_handler(msg_handler, lambda msg: finish_clone_pass(msg, bot, path_to_user_folder))
