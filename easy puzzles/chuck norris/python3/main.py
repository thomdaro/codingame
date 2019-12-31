import sys
import math

message = input()
raw_bin_message = map(bin, bytearray(message, 'utf8'))
bin_message = ""

# process each character
for char in raw_bin_message:
    # remove '0b' header
    char = char.replace("0b","")
    # backfill with zeroes to make seven-digit representation
    if (len(char) < 7):
        char = "0" * (7 - len(char)) + char
    bin_message += char

series_digit = bin_message[0]
digit_count = 1
answer = ("0 " if series_digit == str(1) else "00 ")

for digit in bin_message[1:]:
    if (digit == series_digit):
        digit_count += 1
    else:
        answer += "0" * digit_count + " " + ("0 " if digit == str(1) else "00 ")
        series_digit = digit
        digit_count = 1
        
# add final count for last series since digit-change condition above never trips
answer += "0" * digit_count
    
print(str(answer))