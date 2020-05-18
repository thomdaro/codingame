# Information for "Ghost Legs"

### Introduction and Example

Ghost Legs is a sort of lottery game that has boards that look something like this:

    A  B  C
    |  |  |
    |--|  |
    |  |--|
    |  |--|
    |  |  |
    1  2  3
    
The player chooses a starting point from the top row and a potential endpoint on the bottom row, then traces from the lane downward from  their starting point. When they reach a path that moves left or right, they switch lanes. The win condition occurs if the player ends up at their predicted endpoint. Every starting point has a unique endpoint, so a random guess has an equivalently random chance of being correct.

This problem asks us to take a Ghost Legs diagram and print out all unique start-end pairs. We can use loops, some try-except clauses, and general ASCII processing to accomplish this.

### Input Format

A typical test case input looks like this.

* __Line 1__: integers `W` and `H`, which tell you the width and height of the diagram.
* __Next `H` Lines__: The diagram (see example above.)

### Code Walkthrough

As usual, we start by processing our input and storing all the needed information in appropriately defined variables. `w` and `h` will be useful for loops later. We read the starting inputs into their own array, then the body of the chart into a 2D array to follow each lane from start to finish. Endpoints get their own array for indexing, and the `results` array is initialized.

    w, h = [int(i) for i in input().split()]
    starts = [x for x in input().split('  ')]

    lines = []
    for i in range(1, h-1):
        lines.append(input())

    ends = [x for x in input().split('  ')]
    results = []
    
We use `i` to index the starting position of our "cursor", which will walk down the lane line-by-line. If we see a dash to the left of the current lane in any row, we move left and walk down that lane. The `try`-`except` block with `IndexError` as its exception condition is necessary to prevent checking before the start of the string that represents a row of the diagram.
    
    for i in range(len(starts)):
        pos = i * 3
        
        for line in lines:
        try:
            if line[pos-1] == '-':
                pos -= 3
                continue
        except IndexError:
            pass

If no pipe is found on the left, we check the right and move accordingly.

    try:
        if line[pos+1] == '-':
            pos += 3
            continue
    except IndexError:
        pass
        
Once the bottom is reached, we pair our starting position with the resultant end character and add it to our `results` array.

    results.append(str(starts[i]) + str(ends[int(pos / 3)]))
    
Original Codingame Problem

https://www.codingame.com/training/easy/ghost-legs
