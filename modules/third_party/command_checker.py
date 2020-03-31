from re import compile

def command_checker(text, num_of_chunk, can_be_one_chunk_or_not):
	exception_chars = '!@#$&~%*()\[\]}{\'\\\":;><`.'
	find_exceptions = compile('([{}])'.format(str(exception_chars)))
	res = find_exceptions.findall(text)
	if can_be_one_chunk_or_not:
		if (len(text.split()) <= num_of_chunk) and (str(res) == '[]') and (text.find("//") == -1):
			return True
		else:
			return False
	else:
		if (len(text.split()) == num_of_chunk) and (str(res) == '[]') and (text.find("//") == -1):
			return True
		else:
			return False