import os
import gnupg
from del_mess import del_mess


def touch_main(message, bot_old):
	global bot
	global way
	global name

	bot = bot_old
	command = message.text.split()
	way = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id)
	msg = None
	
	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]

		if os.path.isfile(way +'/'+ name+'.gpg'):
			msg = bot.send_message(message.chat.id,'Файл с таким названием в этой папке уже существует.\n\n')

		else:
			if os.path.isdir(way +'/'+ name):
				msg = bot.send_message(message.chat.id,'Папка с таким названием уже сужествует в этой директории.\n\n')
							
			else:
				part = name.split('/')

				if len(part) < 9:
					msg_handler = bot.send_message(message.chat.id,'Отправте свою запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')

					try:
						bot.register_next_step_handler(msg_handler, touch_pass_query)

					except TypeError as e:
						msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
						del_mess(msg, bot, 4)
						return

				else:
					msg = bot.send_message(message.chat.id,'Вы хотите создать очень много папок. Макс. глубина - 7 папок. Зачем вам столько -.-')

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /touch папка/имя_записи')

	del_mess(msg, bot, 2)


def touch_pass_query(message):
	val_old = '/'
	part = name.split('/')
	
	if not os.path.isdir(way + '/' + '/'.join(part[:-1])):
		os.makedirs(way + '/'+'/'.join(part[:-1]))
	
	gpg = gnupg.GPG()
	gpg.encrypt(
        message.text,
        recipients=['user_'+str(message.from_user.id)],
        output=way + '/' + name + '.gpg',
    )
	
	msg = bot.send_message(message.chat.id,'Запись ' + name + ' добавлена.')
	
	del_mess(msg, bot, 4)
