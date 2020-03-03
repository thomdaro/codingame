import sys
import math


n = int(input())

if n == 0:
    print("0")
    sys.exit()
    
# Set threshold to 1 above the max
closest = 5527

for i in input().split():
    t = int(i)
    # Compare absolute values, change to positive if necessary
    if abs(t) < abs(closest) or t == abs(closest):
        closest = t

print(str(closest))
