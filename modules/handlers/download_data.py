from shutil import make_archive

def download_data_main(message, bot):
	path_to_users_folder = '/home/sepezho/Documents/Seppass/Users_folder/'
	make_archive(path_to_users_folder+'user_'+str(message.from_user.id)+'_data_to_download', 'zip', path_to_users_folder+'user_'+str(message.from_user.id))