words = ["bella", "label", "roller"]
words = ["cool", "lock", "cook"]

def find_letters(words):
	
	res = []
	letters = set()
	letter_checker = False
	double_letter = ' '
	double_checker = 1
	
	for word in words:
		if double_letter in word or double_letter == ' ':
			if word.count(double_letter) == 2 or double_letter == ' ':		
				double_checker *= 1
			else:
				double_checker *= 0
		
		for letter in word:
			if word.count(letter) == 2 and double_letter == ' ':
				double_letter = letter
			letters.add(letter)
	
		
	if double_checker:
		res.append(double_letter)
	
	
	for letter in letters:
		for word in words:
			letter_checker = True if letter in word else False
			
			if not letter_checker:
				break
		
		if letter_checker:
			res.append(letter)
			
			
	return sorted(res)
	
	
a = find_letters(words)
print(a)
