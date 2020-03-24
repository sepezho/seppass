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


def git_clone(message, bot, password):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
		msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой репозиторий.')
		bot.register_next_step_handler(msg_handler, lambda msg: clone_repo(msg, bot, path_to_user_folder, password))

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи gitgenssh), и закинте его на свой github.')
		del_mess(msg, bot, 2)
		return


def clone_repo(message, bot, path_to_user_folder, password):
	git_ssh_cmd = path_to_user_folder + '/user_data/ssh_script.sh'
	try:
		if path.isdir(path_to_user_folder+'/main'):
			rmtree(path_to_user_folder+'/main')
		
		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
			Repo.clone_from(str(message.text), path_to_user_folder+'/main')		
			if path.isfile(path_to_user_folder+'/main/gpg_private_key.asc'):
				markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
				markup.add('Да')
				markup.add('Нет')
				msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что хотите поменять gpg ключ на тот, который находися в репозитории?', reply_markup = markup)
				bot.register_next_step_handler(msg_handler, lambda msg: db_change_plus_copy(msg, bot, str(message.from_user.id), password, path_to_user_folder))
			
			else:
				msg = bot.send_message(message.chat.id, 'Я закончил.')
				del_mess(msg, bot, 2)
				return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
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
			del_mess(msg, bot, 4)
			return

	else:
		msg = bot.send_message(message.chat.id, 'Хорошо, оставлю старый ключ.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
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

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return key


def finish_clone_pass(message, bot, path_to_user_folder):
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да')
	markup.add('Нет')
	markup.add('Отмена')

	msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что этот пароль правильный?\n\n'+message.text, reply_markup = markup)
	bot.register_next_step_handler(msg_handler, lambda msg: write_pass_in_nothing(msg, bot, message.text, path_to_user_folder))


def write_pass_in_nothing(message, bot, password, path_to_user_folder):
	if message.text == 'Да':
		try:
			with open(path_to_user_folder+'/user_data/Nothing.txt', 'w') as f:
				f.write(password)
			msg = bot.send_message(message.chat.id, 'Пароль сохранен.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 4)
			return

		except TypeError as e:
			msg = bot.send_message(message.chat.id, 'Error: '+ str(e), reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 2)
			return

	elif message.text == 'Нет':
		msg_handler = bot.send_message(message.chat.id, 'Введите пароль от нового ключа.\n\n(Если с паролем не уверены, то пока не вышли из бота, измените настройки на вводить пароль при входе, в противном случае я могу сохранить не правельный пароль, и вы не сможете /auth)', reply_markup = types.ReplyKeyboardRemove(selective=False))
		bot.register_next_step_handler(msg_handler, lambda msg: finish_clone_pass(msg, bot))

	else:
		msg = bot.send_message(message.chat.id, 'Я закончил.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return

