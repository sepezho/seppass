import os
import gnupg
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
				bot.send_message(message.chat.id,'Произошла ошибка. Вы уверенны, что назвали путь правильно?')
		else:
			bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /edit папка/имя_записи')
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
	bot.send_message(message.chat.id,'Запись ' + name + ' изменена.')
