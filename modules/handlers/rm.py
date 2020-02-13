import os
import shutil
from ls import ls
from telebot import types

def rm_main(message, bot):
	command = message.text.split()
	if len(command) == 2:
		name = command[1]

		file = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id) +'/'+ name
		if os.path.isfile(file+'.gpg'):
			os.remove(file+'.gpg')
			bot.send_message(message.chat.id, 'Запись '+name+' удалена.')
		elif os.path.isdir(file):
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да, я уверен', 'Нет')
			text = ls(file)
			msg = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить папку '+name+' и все ее содержимое?\n'+ text, reply_markup = markup)
			def finish_rm_folder(message):
				if message.text == 'Да, я уверен':
					shutil.rmtree(file)
					bot.send_message(message.chat.id, 'Папка '+name+', и все ее содержимое удалено.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				else:
					bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			bot.register_next_step_handler(msg, finish_rm_folder)
		else:
			bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
	else:
		bot.send_message(message.chat.id,'Используйте правильный синтаксис: /rm папка/имя_записи')
		return