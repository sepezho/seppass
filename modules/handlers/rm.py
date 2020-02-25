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
			os.remove(file+'.gpg')
			msg = bot.send_message(message.chat.id, 'Запись '+name+' удалена.')
		elif os.path.isdir(file):
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да, я уверен', 'Нет')
			text = ls(file)
			msg = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить папку '+name+' и все ее содержимое?\n'+ text, reply_markup = markup)
			def finish_rm_folder(message):
				msg = None
				if message.text == 'Да, я уверен':
					shutil.rmtree(file)
					msg = bot.send_message(message.chat.id, 'Папка '+name+', и все ее содержимое удалено.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				else:
					msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
				del_mess(msg, bot, 4)
			
			bot.register_next_step_handler(msg, finish_rm_folder)
		else:
			msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
	else:
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /rm папка/имя_записи')
	del_mess(msg, bot, 2)
