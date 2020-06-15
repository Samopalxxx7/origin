import sys


def sum_func(numbs):
	sum = 0
	for i in numbs:
		sum += int(i)
		print('sum ',sum, 'num', i)

digit_string = sys.argv[1]
sum_func(digit_string)
	