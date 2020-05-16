# Information for "Chuck Norris"

### Rules and Implementation

This problem revolces around encoding a message in "unary" using only zeroes. To convert ASCII to unary, we first convert it to 7-bit binary, then look at each digit in the binary representation from most to least significant, i.e. left to right. For each sequence of consecutive zeroes or ones in the binary, we encode a `0` or `00` respectively, followed by a string of zeroes the same length as the sequence. 

As an example, the letter `C` is encoded in 7-bit binary as `1000011`. The first sequence in this binary is `1`, so we encode `00 0` in our unary. The middle sequence is `0000`, which becomes `0 0000`, and the final sequence is `11`, which becomes `00 00`. So `C`, in our unary encoding, is `00 0 0 0000 00 00`.

Implementation is fairly simple. We use `map(bin, bytearray(INPUT))` to transform our message into binary. Using `C` as an example again, this becomes `0b1000011`. We then strip the `0b` header off to get `1000011`. In the case of a character whose binary representation is fewer than 7 bits, say `%` (which gets processed as `100101`), we backfill zeroes to get to 7 digits (i.e. `0100101`). From there, it's a fairly simple matter of processing each series of ones and zeroes and encoding them in the appropriate unary.

### Original Codingame Problem

https://www.codingame.com/training/easy/chuck-norris
