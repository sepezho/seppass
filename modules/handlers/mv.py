import os
import shutil

def mv_main(message, bot):
	command = message.text.split()
	
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
					bot.send_message(message.chat.id, 'Произошла ошибка. Проверте синтаксис и логику.')
					return

				if path_to == '':
					path_to='user_' + str(message.from_user.id)

				bot.send_message(message.chat.id, 'Файл '+path.split('/')[-1]+' перемещен в '+path_to+'.')
			else:
				bot.send_message(message.chat.id, 'В конечной папке уже существует такой файл.')
				return
		elif os.path.isdir(full_path):
			if not(os.path.isdir(full_path_to+'/'+path.split('/')[-1])):
				try:
					shutil.move(full_path, full_path_to+'/'+path.split('/')[-1])
				except:
					bot.send_message(message.chat.id, 'Произошла ошибка. Проверте синтаксис и логику.')
					return
				
				if path_to == '':
					path_to='user_' + str(message.from_user.id)

				bot.send_message(message.chat.id, 'Папка '+path.split('/')[-1]+' перемещена в '+path_to+'.')
			else:
				bot.send_message(message.chat.id, 'В конечной папке уже существует такая папка.')
				return
		else:
			bot.send_message(message.chat.id, 'Такого пути не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /mv начальный_путь конечный_путь (начальный путь указывается с названием перемещаемого папки/файла, конеченый путь - без).')
