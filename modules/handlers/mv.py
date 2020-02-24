import os
import shutil
from del_mess import del_mess

def mv_main(message, bot):
	command = message.text.split()
	msg = None
	if len(command) == 3:

		path = command[1]
		path_to = command[2]
		
		if path[0] == '/':
			path = path[1:]
		if path_to[0] == '/':
			path_to = path_to[1:]
		
		full_path = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ path
		full_path_to = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ path_to

		if os.path.isfile(full_path+'.gpg'):
			if not(os.path.isfile(full_path_to+'/'+path.split('/')[-1]+'.gpg')):
				try:
					shutil.move(full_path+'.gpg', full_path_to+'/'+path.split('/')[-1]+'.gpg')
				except:
					msg = bot.send_message(message.chat.id, 'Произошла ошибка. Проверте синтаксис и логику.')
					del_mess(msg, bot, 2)
					return

				if path_to == '':
					path_to='user_' + str(message.from_user.id)

				msg = bot.send_message(message.chat.id, 'Файл '+path.split('/')[-1]+' перемещен в '+path_to+'.')
			else:
				msg = bot.send_message(message.chat.id, 'В конечной папке уже существует такой файл.')
		elif os.path.isdir(full_path):
			if not(os.path.isdir(full_path_to+'/'+path.split('/')[-1])):
				try:
					shutil.move(full_path, full_path_to+'/'+path.split('/')[-1])
				except:
					msg = bot.send_message(message.chat.id, 'Произошла ошибка. Проверте синтаксис и логику.')
					del_mess(msg, bot, 2)
					return
				
				if path_to == '':
					path_to='user_' + str(message.from_user.id)

				msg = bot.send_message(message.chat.id, 'Папка '+path.split('/')[-1]+' перемещена в '+path_to+'.')
			else:
				msg = bot.send_message(message.chat.id, 'В конечной папке уже существует такая папка.')
		else:
			msg = bot.send_message(message.chat.id, 'Такого пути не существует.')
	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /mv начальный_путь конечный_путь (начальный путь указывается с названием перемещаемого папки/файла, конеченый путь - без).')
	del_mess(msg, bot, 2)