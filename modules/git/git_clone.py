from os import path
from os import system
from git import Git
from git import Repo
from gnupg import GPG
from sqlite3 import connect
from del_mess import del_mess
from shutil import rmtree
from shutil import copy2


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
			if path.isfile(path_to_user_folder+'/main/git_private_key.asc'):
				db_change_plus_copy(str(message.from_user.id), password, path_to_user_folder)

			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 4)
			return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return


def key_edit(key, password, path_to_user_folder):
	gpg = GPG()
	gpg.delete_keys(key, True, passphrase=password)
	gpg.delete_keys(key)

	key_data = open(path_to_user_folder+'/main/git_private_key.asc').read()
	new_key = gpg.import_keys(key_data)
	system('echo RELOADAGENT | gpg-connect-agent')

	return new_key.results[0]['fingerprint']


def db_change_plus_copy(user_id, password, path_to_user_folder):
	conn = connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()

	query = "SELECT Key FROM Users WHERE User_id = 'user_"+user_id+"'"
	key = c.execute(query).fetchall()[0][0]
	query = "UPDATE Users SET Key = '"+key_edit(key, password, path_to_user_folder)+"' WHERE User_id = 'user_"+user_id+"'"

	c.execute(query)
	conn.commit()
	conn.close()

	copy2(path_to_user_folder+'/main/git_private_key.asc', path_to_user_folder+'/user_data/git_private_key.asc')

	return