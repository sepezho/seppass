from os import path
from git import Git
from git import Actor
from git import Repo
from del_mess import del_mess
from shutil import rmtree


def git_init(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
		msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой новый, пустой репозиторий.\nДля этого создайте репу на гитхабе, а потом скопируйте ссылку, ничего более.')
		bot.register_next_step_handler(msg_handler, lambda msg: clone_repo(msg, bot, path_to_user_folder))

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи gitgenssh), и закинте его на свой github.')
		del_mess(msg, bot, 2)
		return


def clone_repo(message, bot, path_to_user_folder):
	git_ssh_cmd = path_to_user_folder + '/user_data/ssh_script.sh'

	try:
		if path.isdir(path_to_user_folder+'/main/.git'):
			rmtree(path_to_user_folder+'/main/.git')

		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):

			repo = Repo.init(path_to_user_folder+'/main')
			repo.index.add('*')

			author = Actor("seppass", "sepezho@gmail.com")
			committer = Actor("seppass", "sepezho@gmail.com")
			repo.index.commit('initial commit', author=author, committer=committer)
			
			origin = repo.create_remote("origin", url=message.text)
			repo.git.push("--set-upstream", origin, repo.head.ref)

			msg = bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 4)
			return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return