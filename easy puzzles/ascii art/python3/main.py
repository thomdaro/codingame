import sys
import math

# use string of the alphabet for indexing
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

l = int(input())
h = int(input())
t = input()

for i in range(h):
    row = input()
    
    # iterate through text, procesing one letter at a time
    for letter in t:
        # find position in the alphabet (capitalize for simplicity)
        position = alpha.find(letter.upper())
        # if we need a question mark
        if position == -1:
            # hardcode question mark position
            answer = answer + row[26 * l:27 * l]
        # grab characters at the letter position
        answer = answer + row[position * l:(position + 1) * l]
    # add a newline to transition to the next row
    answer = answer + "\n"
    
print(answer)