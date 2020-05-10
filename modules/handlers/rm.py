from os import remove
from os import path
from os import walk
from shutil import rmtree
from telebot import types
from ls import ls
from del_mess import del_mess


def rm_main(message, bot):
	command = message.text.split()

	name = command[1]
	if name == '/' or name == '*':
		name = ''
	file = '/Seppass/Users_folder/user_' + str(message.chat.id) +'/main/'+ name

	if path.isfile(file+'.gpg'):
		try:
			remove(file+'.gpg')
			msg = bot.send_message(message.chat.id, 'Запись '+name+' удалена.')
			del_mess(msg, bot, 2)
			return

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
			del_mess(msg, bot, 2)
			return
	
	elif path.isdir(file):
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Да, я уверен')
		markup.add('Нет')

		text = ls(file)
		msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить папку '+name+' и все ее содержимое?\n'+ text, reply_markup = markup)
		bot.register_next_step_handler(msg_handler, lambda msg: finish_rm_folder(msg, bot, file, name))

	else:
		msg = bot.send_message(message.chat.id, 'Такой записи/папки не существует.')
		del_mess(msg, bot, 2)
		return



def finish_rm_folder(message, bot, file, name):
	if message.text == 'Да, я уверен':
		try:
			# for root, dirs, files in walk(file):
			# 	for dir_ in dirs:
			# 		if (root+ '/' +dir_).find(".git") == -1:
			# 			rmtree(root+ '/' +dir_)
			# 	for file in files:
			# 		if (root+ '/' +file).endswith(".gpg"):
			# 			remove(path.join(root, file))
			rmtree(file)
			
			msg = bot.send_message(message.chat.id, 'Папка '+name+', и все ее содержимое удалено.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 4)
			return

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
			del_mess(msg, bot, 4)
			return

	else:
		msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return