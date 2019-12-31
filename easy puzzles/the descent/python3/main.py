import sys
import math

# Tracks the heights of mountains
heights = []

while True:
    for i in range(8):
        mountain_h = int(input())
        heights.append(mountain_h)

    # Get the index of the tallest mountain and zap it
    tallest = heights.index(max(heights))
    print(str(tallest))
    
    # Clear list for next loop
    heights.clear()