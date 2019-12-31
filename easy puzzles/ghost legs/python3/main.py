import sys
import math

w, h = [int(i) for i in input().split()]
# get the characters on the top row, no whitepace
starts = [x for x in input().split('  ')]

# get the lines of the board in a list for iteration later
lines = []
for i in range(1, h-1):
    lines.append(input())
    
ends = [x for x in input().split('  ')]
results = []

for i in range(len(starts)):
    # pipe is at (index of start * 3)
    pos = i * 3
    # walk down the board line-by-line
    for line in lines:
        
        # try-except blocks catch any index errors which may result
        # from checking left of the leftmost pipe (same for right)
        try:
            if line[pos-1] == '-':
                # move to the next pipe left if a connector is found
                pos -= 3
                continue
        except IndexError:
            pass
        # same process for right side
        try:
            if line[pos+1] == '-':
                pos += 3
                continue
        except IndexError:
            pass
    # match up starting character with bottom character at ending position
    results.append(str(starts[i]) + str(ends[int(pos / 3)]))

for result in results:
    print(str(result))