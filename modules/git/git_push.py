from os import path
from git import Git
from git import Repo
from git import Actor
from del_mess import del_mess


def git_push_main(message, bot):
	path_to_user_folder = '/Seppass/Users_folder/user_'+str(message.chat.id)

	if path.isdir(path_to_user_folder+'/main/.git'):
		if path.isfile(path_to_user_folder+'/user_data/token.txt'):
			push_to_repo(message, bot, path_to_user_folder)

		else:
			msg = bot.send_message(message.chat.id, 'Для начала создайте token (при помощи /gittoken).')
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id, 'Для начала привяжите репу к вашему gitHub, при помощи /gitinit или /gitclone.')
		del_mess(msg, bot, 2)
		return



def push_to_repo(message, bot, path_to_user_folder):

	try:
		with open(path_to_user_folder+'/user_data/token.txt', 'r') as f:
			token = f.read()
		with Git().custom_environment(HTTPS_REMOTE_URL='https://'+token+':x-oauth-basic@'+message.text[8:]):
			repo = Repo(path_to_user_folder+'/main')
			author = Actor("seppass", "sepezho@gmail.com")
			committer = Actor("seppass", "sepezho@gmail.com")
			repo.index.add('*')
			repo.index.commit('initial commit', author=author, committer=committer)
			origin = repo.remote(name = 'origin')
			origin.push()
			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 2)
			return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return
