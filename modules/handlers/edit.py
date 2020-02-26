import os
import gnupg
from del_mess import del_mess


def edit_main(message, bot_old):
	global bot
	global name
	global file
	bot = bot_old
	command = message.text.split()
	msg = None
	
	if len(command) == 2:
		name = command[1]
		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name

		if os.path.isfile(file+'.gpg'):
			msg_handler = bot.send_message(message.chat.id,'Отправте новую запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
			
			try:
				bot.register_next_step_handler(msg_handler, rm_and_create_file)
				msg = bot.send_message(message.chat.id,'Запись ' + name + ' изменена.')

			except TypeError as e:
				msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
				del_mess(msg, bot, 4)
				return

		else:
			msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /edit папка/имя_записи')
	del_mess(msg, bot, 2)


def rm_and_create_file(message):
	gpg = gnupg.GPG()
	os.remove(file+'.gpg')
	gpg.encrypt(
        message.text,
        recipients=['user_'+str(message.from_user.id)],
        output= file + '.gpg',
    )