import sys
import math

n = int(input())
solns = []

for i in range(1,n+1):
    
    check = (n*(n+i))/i
    if check.is_integer():
        solns.append((int((n*(n+i))/i), n+i))

for soln in solns:
    print("1/" + str(n) + " = 1/" + str(soln[0]) + " + 1/" + str(soln[1]))