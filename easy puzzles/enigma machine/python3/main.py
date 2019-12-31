import sys
import math

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

operation = input()
shift_amt = int(input())

rotors = []
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()

print("orignal: " + message, file=sys.stderr)

if operation == "ENCODE":
    
    shifted = ""
    for c in message:
        shifted += alpha[(alpha.index(c) + shift_amt) % 26]
        shift_amt += 1
        
    print("shifted: " + shifted, file=sys.stderr)
    
    for rotor in rotors:
        rotated = ""
        for char in shifted:
            rotated += rotor[alpha.index(char)]
        shifted = rotated
        print("rotated: " + rotated, file=sys.stderr)
        
    print(rotated)

elif operation == "DECODE":
    
    rotors.reverse()
    
    for rotor in rotors:
        rotated = ""
        for char in message:
            rotated += alpha[rotor.index(char)]
        message = rotated
        print("rotated: " + rotated, file=sys.stderr)
        
    shifted = ""
    
    for c in message:
        shifted += alpha[(alpha.index(c) - shift_amt) % 26]
        shift_amt += 1
        
    print("shifted: " + shifted, file=sys.stderr)
    
    print(shifted)


# print(, file=sys.stderr)