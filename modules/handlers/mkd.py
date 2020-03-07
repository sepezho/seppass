import os
from ls import ls
from del_mess import del_mess


def mkd_main(message, bot):
	command = message.text.split()
	way = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)
	msg = None
	
	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]
		part = name.split('/')

		if len(part) < 9:
			if os.path.isdir(way+'/'+name):
				msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.\n\n')

			else:
				if os.path.isfile(way +'/'+ name+'.gpg'):
					msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.\n\n')

				else:
					try:
						os.makedirs(way+'/'+name)
						msg = bot.send_message(message.chat.id,'Папка '+name+' создана.')

					except TypeError as e:
						msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		else:
			msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /mkd папка/имя_записи')

	del_mess(msg, bot, 2)
