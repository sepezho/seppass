from os import path
from git import Git
from git import Repo
from del_mess import del_mess


def git_pull(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)
	if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
		pull_to_repo(message, bot, path_to_user_folder)

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи gitgenssh), и закинте его на свой github.')
		del_mess(msg, bot, 2)
		return


def pull_to_repo(message, bot, path_to_user_folder):
	git_ssh_cmd = path_to_user_folder + '/user_data/ssh_script.sh'

	try:
		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
			repo = Repo(path_to_user_folder+'/main')
			
			origin = repo.remote(name = 'origin')
			origin.pull()

			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 2)
			return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return