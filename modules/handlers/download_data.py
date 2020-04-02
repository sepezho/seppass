from os import remove
from shutil import make_archive

from del_mess import del_mess

def download_data_main(message, bot):
	path_to_users_folder = '/home/sepezho/Documents/Seppass/Users_folder/'
	zip_file_name = path_to_users_folder+'user_'+str(message.from_user.id)+'_data_to_download'
	
	try:
		make_archive(zip_file_name, 'zip', path_to_users_folder+'user_'+str(message.from_user.id))
		zip_archive = open(zip_file_name+'.zip', 'rb')
		bot.send_message(message.chat.id, 'Вот все ваши данные, как они есть.')
		msg = bot.send_document(message.chat.id, zip_archive)
		zip_archive.close()
		remove(zip_file_name+'.zip')
		del_mess(msg, bot, 3)
		return

	except:
		msg = bot.send_message(message.chat.id, 'Произошла ошибка.')
		del_mess(msg, bot, 2)
		return
