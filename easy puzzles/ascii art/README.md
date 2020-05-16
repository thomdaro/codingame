# Information for "Ascii Art"

### Rules and Implementation

The objective of this program is straightforward, but the way the input is given makes the process more interesting than one might expect.
The objective is to take a string and a given ASCII art alphabet, then reproduce the string with said alphabet. Input for a test case 
is as follows:

* __Line 1__: `L`, the width of a letter plus a space on the right.
* __Line 2__: `H`, the height of a letter.
* __Line 3__: `T`, the text to be reproduced.
* __Lines 4-X__: `H` lines of symbols, which create the ASCII alphabet, including a question mark at the end for non-alpabet characters.

Printing `T` in ASCII is simple enough. Going line by line down the given symbols, we print the first line of the ASCII text by getting
the `position` of each letter in the alphabet, then multiplying that position by the `width` and printing the next `width` characters.
The position of the question mark is hardcoded in if a character is not found in the default alphabet string.

### Example Test Case

Input for the first supplied test case is as follows:

    4
    5
    E
     #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### 
    # # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # 
    ### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## 
    # # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       
    # # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  
    
Here we see that the letters are four characters wide (including the right-sight buffer space), five characters high, and the string we
want to reproduce is just `E`. E is at position 4 in the alphabet, so for each line of symbols, we move `4 * 4 = 16` spaces over and
print `4` characters plus a newline. This gives us:

    ### 
    #   
    ##  
    #   
    ### 
    
Which is the correct output.

### Original Codingame Problem

https://www.codingame.com/ide/puzzle/ascii-art
