from os import path
from git import Git
from git import Repo
from del_mess import del_mess


def git_pull_main(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	if path.isdir(path_to_user_folder+'/main/.git'):
		if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
			pull_to_repo(message, bot, path_to_user_folder)

		else:
			msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи gitgenssh), и закинте его на свой github.')
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id, 'Для начала привяжите репу к вашему gitHub, при помощи /gitinit или /gitclone.')
		del_mess(msg, bot, 2)
		return

def pull_to_repo(message, bot, path_to_user_folder):

	try:
		with open(path_to_user_folder+'/user_data/token.txt', 'r') as f:
			token = f.read()
		with Git().custom_environment(HTTPS_REMOTE_URL='https://'+token+':x-oauth-basic@'+message.text[8:]):
			repo = Repo(path_to_user_folder+'/main')
			origin = repo.remote(name = 'origin')
			origin.pull()
			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 2)
			return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return
