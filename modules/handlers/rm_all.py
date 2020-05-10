from shutil import rmtree
from os import mkdir
from telebot import types
from ls import ls
from del_mess import del_mess


def rm_all_main(message, bot):
	folder = '/Seppass/Users_folder/user_' + str(message.chat.id) +'/main'

	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('Да, я уверен')
	markup.add('Нет')

	text = ls(folder)
	msg_handler = bot.send_message(message.chat.id, 'Вы уверены, что хотите удалить все файлы (Включая скрытые файлы и папки, которые не отображаются здесь, такие как .git)?\n'+ text, reply_markup = markup)
	bot.register_next_step_handler(msg_handler, lambda msg: rm_all_action(msg, bot, folder))


def rm_all_action(message, bot, folder):
	if message.text == 'Да, я уверен':
		try:
			rmtree(folder)
			mkdir(folder)

			msg = bot.send_message(message.chat.id, 'Все файлы удалены.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 4)
			return

		except:
			msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 4)
			return
	
	else:
		msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return