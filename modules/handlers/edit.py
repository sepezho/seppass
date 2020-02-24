import os
import gnupg
from del_mess import del_mess

def edit_main(message, bot_old):
	global bot
	bot = bot_old
	command = message.text.split()
	if len(command) == 2:
		global name
		name = command[1]
		global file
		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name
		if os.path.isfile(file+'.gpg'):
			msg = bot.send_message(message.chat.id,'Отправте новую запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
			try:
				bot.register_next_step_handler(msg, rm_and_create_file)
			except:
				msg = bot.send_message(message.chat.id,'Произошла ошибка. Вы уверенны, что назвали путь правильно?')
				del_mess(msg, bot, 4)
		else:
			msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
			del_mess(msg, bot, 2)
	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /edit папка/имя_записи')
		del_mess(msg, bot, 2)
		return

def rm_and_create_file(message):
	global file
	gpg = gnupg.GPG()
	os.remove(file+'.gpg')
	gpg.encrypt(
        message.text,
        # recipients=['user_'+user_id],
        recipients='sepezho',
        output= file + '.gpg',
    )
	msg = bot.send_message(message.chat.id,'Запись ' + name + ' изменена.')
	del_mess(msg, bot, 4)
