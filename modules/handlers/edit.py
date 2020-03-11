from os import remove
from os import path
from gnupg import GPG
from del_mess import del_mess


def edit_main(message, bot):
	command = message.text.split()
	
	if (len(command) == 2) and (command[1].find('//') == -1) and (command[1].find('.') == -1) and (command[1][0] != '/') and (command[1][-1] != '/'):
		name = command[1]
		file = '/home/sepezho/Documents/Seppass/Users_folder/user_' + str(message.from_user.id) +'/main/'+ name

		if path.isfile(file+'.gpg'):
			msg_handler = bot.send_message(message.chat.id,'Отправте новую запись (не бойтесь, за ее сохранность, я ее удалю из ваших сообщений).')
			bot.register_next_step_handler(msg_handler, lambda msg: rm_and_create_file(msg, bot, file, name))
		
		else:
			msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
			del_mess(msg, bot, 2)
			return

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /edit папка/имя_записи')
		del_mess(msg, bot, 2)
		return

def rm_and_create_file(message, bot, file, name):
	try:
		gpg = GPG()
		remove(file+'.gpg')
		gpg.encrypt(
	        message.text,
	        recipients=['user_'+str(message.from_user.id)],
	        output= file + '.gpg',
	    )
		
		msg = bot.send_message(message.chat.id,'Запись ' + name + ' изменена.')
		del_mess(msg, bot, 2)
		return

	except TypeError as e:
		msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
		del_mess(msg, bot, 4)
		return
