import sqlite3
from settings import settings_begin_mess
from main import main

def auth_main(message, bot):
	conn = sqlite3.connect('DataBase.db', check_same_thread=False)
	c = conn.cursor()
	query = "SELECT COUNT(*) FROM Users WHERE User_id = '"+str(message.from_user.id)+"'"
	c.execute(query)

	if c.fetchone() == (0,):
		settings_begin_mess(message, bot, False, None)
	else:
		main(message, bot)

	conn.commit()
	conn.close()