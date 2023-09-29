import random
import array
MAX_LEN = 7

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

COMBINED_LIST = DIGITS + UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + SYMBOLS

random_digit = random.choice(DIGITS)
random_upper = random.choice(UPPERCASE_CHARACTERS)
random_lower = random.choice(LOWERCASE_CHARACTERS)
random_symbol = random.choice(SYMBOLS)

temp_pass = random_digit + random_upper + random_lower + random_symbol

for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)

	
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
print(password)
