from os import path
from shutil import move
from del_mess import del_mess

def mv_main(message, bot):
	command = message.text.split()

	path = command[1]
	path_to = command[2]
	
	if path[0] == '/':
		path = path[1:]
	if path_to[0] == '/':
		path_to = path_to[1:]
	
	full_path = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id) +'/main/'+ path
	full_path_to = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id) +'/main/'+ path_to

	if path.isfile(full_path+'.gpg'):
		if not(path.isfile(full_path_to+'/'+path.split('/')[-1]+'.gpg')):
			if not(path.isdir(full_path_to+'/'+path.split('/')[-1])):
				try:
					move(full_path+'.gpg', full_path_to+'/'+path.split('/')[-1]+'.gpg')
				
				except TypeError as e:
					msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
					del_mess(msg, bot, 2)
					return

				if path_to == '':
					path_to = '/main'

				msg = bot.send_message(message.chat.id, 'Файл '+path.split('/')[-1]+' перемещен в '+path_to+'.')
				del_mess(msg, bot, 2)
				return
			
			else:
				msg = bot.send_message(message.chat.id,'Папка с таким названием в конечной директории уже существует.\n\n')
				del_mess(msg, bot, 2)
				return
		else:
			msg = bot.send_message(message.chat.id, 'В конечной папке уже существует такой файл.')
			del_mess(msg, bot, 2)
			return

	elif path.isdir(full_path):
		if not(path.isdir(full_path_to+'/'+path.split('/')[-1])):
			if not(path.isfile(full_path_to+'/'+path.split('/')[-1]+'.gpg')):
				try:
					move(full_path, full_path_to+'/'+path.split('/')[-1])
				
				except TypeError as e:
					msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
					del_mess(msg, bot, 2)
					return
				
				if path_to == '':
					path_to = '/main'

				msg = bot.send_message(message.chat.id, 'Папка '+path.split('/')[-1]+' перемещена в '+path_to+'.')
				del_mess(msg, bot, 2)
				return

			else:
				msg = bot.send_message(message.chat.id,'Файл с таким названием в конечной папке уже существует.\n\n')
				del_mess(msg, bot, 2)
				return
		else:
			msg = bot.send_message(message.chat.id, 'В конечной директории уже существует такая папка.')
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id, 'Такого пути не существует.')
		del_mess(msg, bot, 2)
		return
