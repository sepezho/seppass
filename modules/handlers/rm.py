import os
import shutil
from ls import ls
from telebot import types
from del_mess import del_mess


def rm_main(message, bot):
	command = message.text.split()
	msg = None
	
	if len(command) == 2:
		name = command[1]
		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name

		if os.path.isfile(file+'.gpg'):
			try:
				os.remove(file+'.gpg')
				msg = bot.send_message(message.chat.id, 'Запись '+name+' удалена.')

			except TypeError as e:
				msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
				del_mess(msg, bot, 3)
				return
		
		elif os.path.isdir(file):
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да, я уверен', 'Нет')
			
			try:
				text = ls(file)
			
			except TypeError as e:
				msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
				del_mess(msg, bot, 2)
				return

			def finish_rm_folder(message):
				if message.text == 'Да, я уверен':
					try:
						shutil.rmtree(file)
						msg = bot.send_message(message.chat.id, 'Папка '+name+', и все ее содержимое удалено.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			
					except TypeError as e:
						msg = bot.send_message(message.chat.id, 'Error: '+ str(e))
						del_mess(msg, bot, 4)
						return

				else:
					msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))

				del_mess(msg, bot, 4)

			msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить папку '+name+' и все ее содержимое?\n'+ text, reply_markup = markup)
			bot.register_next_step_handler(msg_handler, finish_rm_folder)

		else:
			msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')

	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /rm папка/имя_записи')

	del_mess(msg, bot, 2)
