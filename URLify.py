def URLify(string):
	list = ""
	for c in string:
		if c == ' ':
			list.append("%20")
		else:
			list.append(c)
	
	return str(list)