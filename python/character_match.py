# Don't forget to run your tests!

def is_character_match(string1, string2):
	string1_list = list(string1.casefold().replace(' ',''))
	string2_list = list(string2.casefold().replace(' ',''))
	
	if len(string1_list) != len(string2_list):
		return False
	
	for char in string1_list:
		if char in string2_list:
			string2_list.remove(char)
	
	if len(string2_list) != 0:
		return False
	else:
		return True


#print(is_character_match('charm', 'march')) # True
#print(is_character_match('zach', 'attack')) # False
#rint(is_character_match('CharM', 'mARcH')) # True
#print(is_character_match('abcde2', 'c2abed')) # True

#print(is_character_match('Anna Madrigal', 'A man and a girl')) # True
