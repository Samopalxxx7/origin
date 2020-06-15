import sys

nums = int(sys.argv[1])

for i in range(1,nums+1):
	print(' ' * (nums - i)+('#'*i))