from os import path
from git import Git
from git import Repo
from del_mess import del_mess
from shutil import rmtree


def git_clone(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
		msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой репозиторий.')
		bot.register_next_step_handler(msg_handler, lambda msg: clone_repo(msg, bot, path_to_user_folder))

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи gitgenssh), и закинте его на свой github.')
		del_mess(msg, bot, 2)
		return


def clone_repo(message, bot, path_to_user_folder):
	git_ssh_cmd = path_to_user_folder + '/user_data/ssh_script.sh'

	try:
		if path.isdir(path_to_user_folder+'/main'):
			rmtree(path_to_user_folder+'/main')
		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
			Repo.clone_from(str(message.text), path_to_user_folder+'/main')		
			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 4)
			return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return