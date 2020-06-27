import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

delta = pow(b, 2) - 4 * a * c

if delta < 0:
    print(0)
elif delta == 0:
    x0 = -b / 2 * a
    print(1,'\n',x0)
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(2,'\n',x1, x2)