import sys
import math

w, h, count_x, count_y = [int(i) for i in input().split()]
xs = [0]
ys = [0]

# add all x's, including the right edge of the rectangle
for i in input().split():
    x = int(i)
    xs.append(x)
xs.append(w)

# same for y's
for i in input().split():
    y = int(i)
    ys.append(y)
ys.append(h)
    
x_diffs = []
y_diffs = []

# add all possible differences between x's
# (length is sum of the first count_x natural numbers)
for i in range(len(xs)-1):
    for j in range(i+1, len(xs)):
        x_diffs.append(xs[j]-xs[i])
        
# could use count_x and count_y here but it would be confusing
for i in range(len(ys)-1):
    for j in range(i+1, len(ys)):
        y_diffs.append(ys[j]-ys[i])
        
squares = 0
        
# squares occur x_dist = y_dist for any pair of distances
for x_diff in x_diffs:
    squares += y_diffs.count(x_diff)

print(str(squares))