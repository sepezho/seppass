from del_mess import del_mess
from sqlite3 import connect
from telebot import types

def git_token_main(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton('Как создать токен?', url='https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line'))

	bot.send_message(message.chat.id, 'При создании токена обязательно разрешите доступ к приватным репозиториям', reply_markup=markup)

	markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup1.add('Выход.')

	msg_handler = bot.send_message(message.chat.id, 'Отправьте мне GitHub access token.', reply_markup=markup1)
	bot.register_next_step_handler(msg_handler, lambda msg: save_token(msg, bot, path_to_user_folder))

def save_token(message, bot, path_to_user_folder):
	if len(message.text) == 40:
		with open(path_to_user_folder+'/user_data/token.txt', 'w') as f:
			f.write(message.text)
		msg = bot.send_message(message.chat.id, 'Я закончил.',  reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 5)
		return
	else:
		msg = bot.send_message(message.chat.id, 'Отмена.',  reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 5)
		return
