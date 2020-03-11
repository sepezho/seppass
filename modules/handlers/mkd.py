from os import makedirs
from os import path
from del_mess import del_mess


def mkd_main(message, bot):
	command = message.text.split()
	way = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)+'/main/'
	
	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]
		if len(name.split('/')) < 9:
			if not path.isdir(way+'/'+name):
				if not path.isfile(way +'/'+ name+'.gpg'):
					try:
						makedirs(way+'/'+name)
						msg = bot.send_message(message.chat.id,'Папка '+name+' создана.')
						del_mess(msg, bot, 2)
						return
						
					except TypeError as e:
						msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
						del_mess(msg, bot, 2)
						return
				else:
					msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.\n\n')
					del_mess(msg, bot, 2)
					return
			else:
				msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.\n\n')
				del_mess(msg, bot, 2)
				return
		else:
			msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')
			del_mess(msg, bot, 2)
			return
	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /mkd папка/имя_записи')
		del_mess(msg, bot, 2)
		return
