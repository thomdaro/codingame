import sys
import math

n = int(input())
l = int(input())
room = [[] for _ in range(n)]
candle_psns = []

print("layout: ", file=sys.stderr)

for i in range(n):
    line = input()
    for j in range(n*2-1):
        char = line[j]
        if char != ' ':
            if char == "X":
                room[i].append(0)
                print("X", end=" ", file=sys.stderr)
            elif char == "C":
                room[i].append(l)
                candle_psns.append((i, j // 2))
                print("C", end=" ",file=sys.stderr)
    print("\b", file=sys.stderr)
    
print("\nbase light lvl: " + str(l), file=sys.stderr)

for pos in candle_psns:
    for i in range(1,l):
        for j in range(-i,i+1):
            for k in range(-i,i+1):
                try:
                    if pos[0]+j >= 0 and pos[1]+k >= 0 and math.sqrt(j**2 + k**2) >= i:
                        room[pos[0]+j][pos[1]+k] += l-i
                except IndexError:
                    pass
   
print("\nlightmap: ", file=sys.stderr)
for line in room:
    for char in line:
        print(char, file=sys.stderr, end=" ")
    print("\b", file=sys.stderr)

res = 0
for line in room:
    for char in line:
        if char == 0:
            res += 1

print(file=sys.stderr)
print(str(res))