import sys
import math


n = int(input())
# Set threshold to 1 above the max
closest = 5527

for i in input().split():
    t = int(i)
    # Compare absolute values, change to positive if necessary
    if abs(t) < abs(closest) or (t == abs(closest) and t > 0):
        closest = t
        
# If no input was received, output 0
if closest == 5527:
    closest = 0

print(str(closest))