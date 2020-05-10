from re import match
from re import escape
import string

def command_checker(text, num_of_chunk, can_be_one_chunk_or_not):
	#Запилил провер очку регуляркой на допустимые символы
	pat = '^[A-Za-z0-9\s/]+$'.format(escape(string.punctuation))
	if can_be_one_chunk_or_not:
		if (len(text.split()) <= num_of_chunk) and (text.find("//") == -1) and (bool(match(pat, text))):
			return True
		else:
			return False
	else:
		if (len(text.split()) == num_of_chunk) and (text.find("//") == -1) and (bool(match(pat, text))):
			return True
		else:
			return False
