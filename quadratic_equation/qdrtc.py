import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print(a,b,c)

discrim = b**2 - 4*a*c


if discrim <0:
	print("without sqrt")
elif discrim == 0:
	x1 = -b / (2*a)
	x2 = x1
	print(x1, x2)
else:
	x1 = (-b + math.sqrt(discrim)) / (2 * a)
	x2 = (-b - math.sqrt(discrim)) / (2 * a)
	print("!!!!!!!!!!!!!!!!!!!!!")
	print(math.trunc(x1))
	print(math.trunc(x2))