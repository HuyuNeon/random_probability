import random

digit = input('Digit:')
num = ''
attempt = 0
while not str(num) == '0' * int(digit):
	num = ''
	for i in range(int(digit)):
		num += str(random.randint(0,9))
	attempt += 1
	print(f'Attempt {attempt}:{num}')

print(f'Probability: {1 / attempt}%')