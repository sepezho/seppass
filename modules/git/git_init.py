from os import path
from git import Git
from git import Actor
from git import Repo
from shutil import rmtree
from telebot import types
from del_mess import del_mess


def git_init_main(message, bot):
	path_to_user_folder = '/home/sepezho/Documents/Seppass/Users_folder/user_'+str(message.from_user.id)

	if path.isfile(path_to_user_folder+'/user_data/ssh_key.pub'):
		if not path.isdir(path_to_user_folder+'/main/.git'):
			msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой новый, пустой репозиторий.\nДля этого создайте репу на гитхабе, а потом скопируйте ссылку, и отправьте мне.')
			bot.register_next_step_handler(msg_handler, lambda msg: init_repo(msg, bot, path_to_user_folder))

		else:
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
			markup.add('Да')
			markup.add('Нет')

			msg_handler = bot.send_message(message.chat.id, 'Ваша папка уже является git репозиторием.\n\nВы хотите удалить папку .git, чтобы можно было инициализировать репозиторий заново?', reply_markup = markup)
			bot.register_next_step_handler(msg_handler, lambda msg: question_delete(msg, bot, path_to_user_folder))
			return

	else:
		msg = bot.send_message(message.chat.id, 'Для начала создайте ssh ключ (при помощи /gitgenssh), и закинте его на свой gitHub.')
		del_mess(msg, bot, 2)
		return

def question_delete(message, bot, path_to_user_folder):
	if message.text == 'Да':
		rmtree(path_to_user_folder+'/main/.git')
		msg_handler = bot.send_message(message.chat.id, 'Введите ссылку на свой новый, пустой репозиторий.\nДля этого создайте репу на гитхабе, а потом скопируйте ссылку, и отправьте мне.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		bot.register_next_step_handler(msg_handler, lambda msg: init_repo(msg, bot, path_to_user_folder))

	else:
		msg = bot.send_message(message.chat.id, 'Отмена.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return

def init_repo(message, bot, path_to_user_folder):

	try:
		with open(path_to_user_folder+'/user_data/token.txt', 'r') as f:
			token = f.read()
		with Git().custom_environment(HTTPS_REMOTE_URL='https://'+token+':x-oauth-basic@'+message.text[8:]):
			repo = Repo.init(path_to_user_folder+'/main')
			repo.index.add('*')
			author = Actor("seppass", "sepezho@gmail.com")
			committer = Actor("seppass", "sepezho@gmail.com")
			repo.index.commit('initial commit', author=author, committer=committer)
			origin = repo.create_remote("origin", url='https://'+token+':x-oauth-basic@'+message.text[8:])
			repo.git.push("--set-upstream", origin, repo.head.ref)
			msg = bot.send_message(message.chat.id, 'Я закончил.', reply_markup = types.ReplyKeyboardRemove(selective=False))
			del_mess(msg, bot, 6)
			return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.', reply_markup = types.ReplyKeyboardRemove(selective=False))
		del_mess(msg, bot, 4)
		return
