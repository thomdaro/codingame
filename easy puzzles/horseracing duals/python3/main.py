import sys
import math

n = int(input())
strengths = []
closest = 9999999

for i in range(n):
    pi = int(input())
    strengths.append(pi)
    
strengths.sort()

for i in range(len(strengths) - 1):
    diff = strengths[i+1] - strengths[i]
    if diff < closest:
        closest = diff

print(closest)