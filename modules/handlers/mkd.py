import os
from ls import ls

def mkd_main(message, bot):
	command = message.text.split()
	way = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id)

	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1):
		
		name = command[1]
		if name[-1] == '/':
			name = name[:-1]
		if name[1] == '/':
			name = name[1:]

		part = name.split('/')
		if len(part) < 9:
			if os.path.isdir(way+'/'+name):
				bot.send_message(message.chat.id,'Такая папка уже существует.\n\n' + ls(way+'/'+name))
			else:
				try:
					os.makedirs(way+'/'+name)
					bot.send_message(message.chat.id,'Папка '+name+' создана.')
				except:
					bot.send_message(message.chat.id,'Произошла ошибка. Вы уверенны, что назвали путь правильно?')
		else:
			bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /mkd папка/имя_записи')