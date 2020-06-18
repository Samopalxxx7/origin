import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print(a,b,c)

k2 = b**2 - 4*a*c
print(k2)
x1 = ((-b + math.sqrt(k2))/(2*a))
x2 = ((-b - math.sqrt(k2))/(2*a))
print(int(x1), int(x2))