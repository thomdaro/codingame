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

if operation == "ENCODE":
    
    shifted = ""
    for c in message:
        shifted += alpha[(alpha.index(c) + shift_amt) % 26]
        shift_amt += 1
    
    for rotor in rotors:
        rotated = ""
        for char in shifted:
            rotated += rotor[alpha.index(char)]
        shifted = rotated
        
    print(rotated)

elif operation == "DECODE":
    
    rotors.reverse()
    
    for rotor in rotors:
        rotated = ""
        for char in message:
            rotated += alpha[rotor.index(char)]
        message = rotated
        
    shifted = ""
    
    for c in message:
        shifted += alpha[(alpha.index(c) - shift_amt) % 26]
        shift_amt += 1
            
    print(shifted)
