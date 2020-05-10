from os import path
from shutil import move
from del_mess import del_mess

def mv_main(message, bot):
	command = message.text.split()

	path_from = command[1]
	path_to = command[2]
	
	if path_from[0] == '/':
		path_from = path_from[1:]
	if path_to[0] == '/':
		path_to = path_to[1:]
	
	full_path = '/Seppass/Users_folder/user_' + str(message.chat.id) +'/main/'+ path_from
	full_path_to = '/Seppass/Users_folder/user_' + str(message.chat.id) +'/main/'+ path_to

	if path.isfile(full_path+'.gpg'):
		if not(path.isfile(full_path_to+'/'+path_from.split('/')[-1]+'.gpg')):
			if not(path.isdir(full_path_to+'/'+path_from.split('/')[-1])):
				try:
					move(full_path+'.gpg', full_path_to+'/'+path_from.split('/')[-1]+'.gpg')
				
				except:
					msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
					del_mess(msg, bot, 2)
					return

				if path_to == '':
					path_to = '/main'

				msg = bot.send_message(message.chat.id, 'Файл '+path_from.split('/')[-1]+' перемещен в '+path_to+'.')
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
		if not(path.isdir(full_path_to+'/'+path_from.split('/')[-1])):
			if not(path.isfile(full_path_to+'/'+path_from.split('/')[-1]+'.gpg')):
				try:
					move(full_path, full_path_to+'/'+path_from.split('/')[-1])
				
				except:
					msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
					del_mess(msg, bot, 2)
					return
				
				if path_to == '':
					path_to = '/main'

				msg = bot.send_message(message.chat.id, 'Папка '+path_from.split('/')[-1]+' перемещена в '+path_to+'.')
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
