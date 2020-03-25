import re

def command_checker(message, num_of_chunk):
	exception_chars = '!@#$&~%*()\[\]}{\'\\\":;><`.'
	find_exceptions = re.compile('([{}])'.format(str(exception_chars)))
	res = find_exceptions.findall(message)
	
	if (len(message.split()) == num_of_chunk) and (str(res) == '[]'):
		return True
			
	else:
		return False


