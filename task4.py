numbers = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000,
}


def get_integer_number(numbers, roman_number):
	
	res = 0
	current_num = 1
	
	for i in roman_number:
		if int(current_num) < numbers.get(i):
			res -= numbers.get(i)
			if res < 0:
				res = abs(res)
		else:
			res += numbers.get(i)
			
		current_num = numbers.get(i)
		
		
	return res


print(get_integer_number(numbers, "LXXX"))
