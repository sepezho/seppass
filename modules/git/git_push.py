from os import path
from git import Git
from git import Repo
from del_mess import del_mess


def git_push(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)+'/main'

	if path.isfile(path_to_user_folder+'/user_data/ssh_key'):
		msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой репозиторий.')
		bot.register_next_step_handler(msg_handler, lambda msg: clone_repo(msg, bot, path_to_user_folder))

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи git_gen_ssh), и закинте его на свой github.')
		del_mess(msg, bot, 2)
		return


def clone_repo(message, bot, path_to_user_folder):
	git_ssh_cmd = path_to_user_folder + '/user_data/ssh_script.sh'

	try:
		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
			Repo.clone_from(str(message.text), path_to_user_folder+'/main')		
			bot.send_message(message.chat.id, 'Все, походу.')
			del_mess(msg, bot, 4)
			return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 2)
		return

# --------------------
		# empty_repo = Repo.init(os.path.join(path_to_user_folder, 'empty'))
		# origin = empty_repo.create_remote('origin', message.text)
		# assert origin.exists()
		# assert origin == empty_repo.remotes.origin == empty_repo.remotes['origin']
		# empty_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
		# origin.fetch()
		# origin.pull()
# --------------------




	# origin.push()
	# assert not empty_repo.delete_remote(origin).exists()     # create and delete remotes
	# git_ssh_identity_file = os.path.expanduser(path_to_user_folder + 'ssh_keys/private')
	# git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
	# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
	# 	Repo.clone_from(str(message.text), path_to_user_folder+'/Main')











	# git_ssh_identity_file = os.path.expanduser(path_to_user_folder+'/ssh_keys/private')
	# git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file % '%s  -oIdentitiesOnly=yes -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null "$@"'


	# with open(path_to_user_folder+'/ssh_keys/ssh_script.sh', 'r') as git_ssh_cmd:
	# git_ssh_cmd = 'ssh -i /home/sepezho/Documents/Seppass/Users_folder/user_707939820/ssh_keys/private -oIdentitiesOnly=yes -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null "$@"'


	# git_ssh_identity_file = os.path.expanduser(path_to_user_folder + 'ssh_keys/private')
	# git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
	# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
	# 	Repo.clone_from(str(message.text), path_to_user_folder+'/Main')
	# Repo.clone_from(str(message.text), path_to_user_folder+'/Main', env=dict(GIT_SSH_COMMAND=str(git_ssh_cmd)))
	# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
	# 	print(message.text)
	# 	print(str(git_ssh_cmd))
	# 	print(path_to_user_folder+'/Main')
	# 	Repo.clone_from(message.text, path_to_user_folder+'/Main', branch='origin')




	# repo = Repo(path_to_user_folder+"/Main")
	# repo = git.Repo.clone_from(message.text, os.path.join(path_to_user_folder, 'Main'), branch='master')
	# tst = repo.create_remote('tst', 'https://github.com/sepezhotest/tst.git')
	
	# ssh_executable = os.path.join(path_to_user_folder, 'my_ssh_executable.sh')
	# with repo.git.custom_environment(GIT_SSH=ssh_executable):
	
# ------------------
	# empty_repo = git.Repo.init(os.path.join(path_to_user_folder, 'Main'))
	# origin = empty_repo.create_remote('origin', message.text)
	# empty_repo.create_head('master', origin.refs.master)
	# empty_repo.heads.master.set_tracking_branch(origin.refs.master)
	# empty_repo.heads.master.checkout()
	# empty_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
	# origin.push()
# ------------------

	# ssh_executable = os.path.join(path_to_user_folder+'/ssh_keys', 'ssh_script.sh')
	# with repo.git.custom_environment(GIT_SSH=ssh_executable):

	# 	empty_repo = git.Repo.init(os.path.join(path_to_user_folder, 'Main'))
	# 	origin = empty_repo.create_remote('origin', repo.remotes.origin.url)
	# 	assert origin.exists()
	# 	assert origin == empty_repo.remotes.origin == empty_repo.remotes['origin']
	# 	origin.fetch()                  # assure we actually have data. fetch() returns useful information
	# 	# Setup a local tracking branch of a remote branch
	# 	empty_repo.create_head('master', origin.refs.master)  # create local branch "master" from remote "master"
	# 	empty_repo.heads.master.set_tracking_branch(origin.refs.master)  # set local "master" to track remote "master
	# 	empty_repo.heads.master.checkout()  # checkout local "master" to working tree
	# 	# Three above commands in one:
	# 	empty_repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
	# 	# rename remotes

	# 	# push and pull behaves similarly to `git push|pull`
	# 	origin.pull()

		# origin.push()
		# assert not empty_repo.delete_remote(origin).exists()     # create and delete remotes


	# with open(path_to_user_folder+'/ssh_keys/ssh_script.sh', 'r') as git_ssh_cmd:
	# 	with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
	# 		Repo.clone_from(message.text, path_to_user_folder+'/Main', branch='master', )