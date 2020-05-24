# Information for "Enigma Machine"

### Introduction and Example

The Enigma machine was used during WWII to transmit coded messages, and while cracking the code took considerable effort, we can replicate its encryption process fairly easily. 

Say we start with the string `AAA`. We apply an incrementing Caeser shift to each character – so if we start with a shift of 4, then we shift the first character 4, the second 5, the third 6. This gives us a shifted message of `EFG`.

Enigma relies on a series of gears or rotors to transform its messages. These rotors are just rearrangements of the alphabet, such that between two rotors, there are only a couple (or zero) positions which contain the same letter. We map the shifted message from its standard alphabet positions to the first rotor:

        123
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
        |||
    BDFHJLCPRTXVZNYEIWGAKMUSQO
        123
    
This gives us the rotated message `JLC`, which we can map onto a second rotor from the original alphabet again.
      
      3      1 2
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
      |      | |
    AJDKSIRUXBLHWTMCQGZNPYFVOE
      3      1 2
    
From this, we get `BHD`, which we map onto the third and final rotor.

     1 3   2
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
     | |   |
    EKMFLGDQVZNTOWYHXUSPAIBRCJ
     1 3   2
    
This gives us a final message of `KQF`. We can decode this message by running through the process in reverse: mapping from each rotor to the alphabet, then Caeser shift each character backwards incrementally to get the original message. This problem involves programming a machine that can encrypt and decrypt messages using this method.

### I/O Format

#### Input

* __Line 1:__ `ENCODE` or `DECODE`, indicating the function to perform.
* __Line 2:__ The starting shift `N`.
* __Lines 3-5:__ The three rotors used in the machine.
* __Line 6:__ The message to encode or decode.

Formatting our example like this gives us:

    ENCODE
    4
    BDFHJLCPRTXVZNYEIWGAKMUSQO
    AJDKSIRUXBLHWTMCQGZNPYFVOE
    EKMFLGDQVZNTOWYHXUSPAIBRCJ
    AAA

#### Output

The encoded or decoded message. For the sake of consistency, it would look like this:

    KQF
    
### Code Walkthrough

Input processing is especially important for this problem. Storing the rotors in a list allows us to loop through them sequentially, so we can iterate over a potentially very long series of rotors rather than hard-coding them in.

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    operation = input()
    shift_amt = int(input())

    rotors = []
    for i in range(3):
        rotor = input()
        rotors.append(rotor)
    message = input()
    
If we're encoding the message, we need to start by shifting it. This can be done with a simple loop and some modulo division, to account for shifts that take the character past the end of the alphabet string back around to the front.  
    
    if operation == "ENCODE":
    
    shifted = ""
    for c in message:
        shifted += alpha[(alpha.index(c) + shift_amt) % 26]
        shift_amt += 1
        
This structure iterates over the rotors in order, mapping each character to its respective position on the rotor. The message is then set for the next rotor to modify. After the final rotation, the full encrypted result is printed as output.   
        
    for rotor in rotors:
        rotated = ""
        for char in shifted:
            rotated += rotor[alpha.index(char)]
        shifted = rotated   
        
    print(rotated)        
    
Decoding is a similar process. We iterate over the rotors in reverse order, then Caeser-shift the un-rotated message backwards.

### Original Codingame Problem

https://www.codingame.com/training/easy/encryptiondecryption-of-enigma-machine
