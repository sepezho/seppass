import os
from git import Git
from git import Repo
import git
from telebot import types
from Crypto.PublicKey import RSA

from del_mess import del_mess


def getgit(message, bot_old):
	global bot
	global path
	global path_to_user_folder
	bot = bot_old
	git_ssh_cmd = None

	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)
	path = path_to_user_folder+'/ssh_keys'
	
	# path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_707939820'
	# with open(path+'/ssh_script.sh', 'r') as git_ssh_cmd:
	# 	init('https://github.com/sepezhotest/tst.git', path_to_user_folder+'/Main', path+'/ssh_script.sh', git_ssh_cmd)

	try_to_clone_repo()
	# try:
		# path = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)+'/ssh_keys'
	# 	if not os.path.isdir(path):
 # 			os.makedirs(path)
		
	# 	key = RSA.generate(2048)
	# 	key_pub = None

	# 	with open(path+'/private', 'wb') as content_file:
	# 	    content_file.write(key.exportKey('PEM'))
	# 	    os.chmod(path+'/private', int('0600', base=8))
		
	# 	with open(path+'/public.pub', 'wb') as content_file:
	# 		pubkey = key.publickey()
	# 		key_pub = pubkey.exportKey('OpenSSH')
	# 		content_file.write(pubkey.exportKey('OpenSSH'))
		
	# 	ssh_code = '#!/bin/bash\nssh -i '+path+'/private -oIdentitiesOnly=yes -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null "$@"'
	# 	with open(path+'/ssh_script.sh', 'w') as content_file:
	# 		content_file.write(str(ssh_code))
	# 		os.chmod(path+'/ssh_script.sh', int('0600', base=8))
		
	# 	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	# 	markup.add('Да')
	# 	markup.add('Вернуться')
	# 	msg_handler = bot.send_message(message.chat.id, 'Вот ваш публичный ключ. Сами знаете куда его сувать...\n\n'+key_pub.decode("utf-8")+'\n\nЗакончили?',reply_markup = markup)
	# 	bot.register_next_step_handler(msg_handler, try_to_clone_repo)
	# 	# del_mess(msg, bot, 2)
	# 	return

	# except TypeError as e:
	# 	msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
	# 	del_mess(msg, bot, 2)
	# 	return

def try_to_clone_repo():
	# if message.text == 'Да':
	with open(path+'/ssh_script.sh', 'r') as git_ssh_cmd:
		# path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)
		# init('https://github.com/sepezhotest/tst.git', path_to_user_folder+'/Main', path+'/ssh_script.sh', git_ssh_cmd)
		with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
			repo = Repo.init(path_to_user_folder)
			repo.index.add(['.'])
			repo.index.commit('Initial commit')
			# repo.create_remote('origin')
			repo.remotes.origin.push(repo.refs.master, GIT_SSH_COMMAND=git_ssh_cmd)
				# Repo.clone_from('git@github.com:SEPEZHO/Seppass.git', path_to_user+'/gitRepo', branch='master')

		# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
		# 	repo = Repo.init(path_to_user_folder)
		# 	# repo.index.add('.')
		# 	# repo.index.commit("initial commit")
		    
		# 	origin = repo.remote()
		# 	refs = origin.refs

		# 	for ref in refs:
		# 		if ref.remote_head == "master":
		# 			origin.push()



def init(src_to_remote_repo, path_to_repo, path_to_ssh, git_ssh_cmd):

	# repo = src_to_remote_repo.strip()
	# path = os.path.join(os.getcwd(), path.strip())
	user = {'ssh': git_ssh_cmd, 'name': 'SEPPASS', 'email': 'sepezho@gmail.com'}
	# nothing.update(user)
	# user = nothing

	# os.environ['GIT_SSH'] = user['ssh']

	# if os.path.isdir(path_to_repo):
	#     self.repo = Repo(path_to_repo)
	#     self.repo.git.pull('origin', 'master')
	# else:
    # os.makedirs(path)

	# src_to_remote_repo.config_writer().set_value('user', 'name', user['name']).release()
	# src_to_remote_repo.config_writer().set_value('user', 'email', user['email']).release()
	
	repo = Repo.init(path_to_repo)

	    
	# origin = repo.create_remote('origin', src_to_remote_repo)
	with repo.git.custom_environment(GIT_SSH_COMMAND=user['ssh']):
		repo.index.add('a.py')
		repo.index.commit('commit')
		# git.objects.commit.Commit(repo, user['ssh'], tree='Master')
		info = remote.push()
		# repo.index.push()

	# src_to_remote_repo = Repo.clone_from(src_to_remote_repo, path, env={'GIT_SSH': user['ssh']})
