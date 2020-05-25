# Information for 'Detective Pikaptcha - Ep. 2'

### Introduction and Example

This problem uses mazes similar to Ep. 1, but involves a more complex traversal. We're given a maze layout, a side to follow, and a starting position and direction. Starting from that position, we walk forward, following the given wall until reaching the starting point again. The end result should be the maze layout, but each walkable space contains a number indicating the number of times it was walked over in the traversal.

Maze layouts are given with three different characters: `0` for walkable spaces, `#` for impassable walls, and either `^`, `>`, `v`, or `<` to indicate the starting position and direction of our traversal. Here's a small example:

    >000#
    #0#00
    00#0#
    
Following the left wall, we walk until reaching the starting position again, giving us the following output:

    1322#
    #2#31
    12#1#
    
Note that our program runtime is limited to two seconds even for large cases, so we need a relatively efficient method of traversal and marking paths.

### I/O Format

#### Input

*__Line 1:__ Two integers `width` and `height` for the dimensions of the maze.
*__Next `height` Lines:__ A string of length `width` containing one row of the maze, with the given character layout.
*__Next line:__ A character `R` or `L` indicating which side to follow.

#### Output

`height` lines of length `width` containing the transformed grid, consisting of walls `#` and integers `0`-`4` indicating the number of times a tile was traversed.

### Code Walkthrough

Because we need to keep track of our current position and direction during traversal, we create two additional variables to store this data. The maze is read in as strings, but is transformed into a 2D array for easier traversal and processing. We'll be modifying the maze data as we traverse, and because strings are immutable in Python, this is much easier to do with a list.

    width, height = [int(i) for i in input().split()]
    maze = [[] for _ in range(height)]
    pos = (-1, -1)
    dirn = ""

    for i in range(height):
        line = input()
        for char in line:
            maze[i].append(char)

    side = input() 
 
For each direction, we perform a check to see if there an open space in that direction. If so, we increment its traversal count by 1 and return the new positional data, as well as setting our current direction to the one just checked / moved.
 
    def check_east(pos):
        try:
            if maze[pos[0]][pos[1]+1] != "#":
                maze[pos[0]][pos[1]+1] = str(int(maze[pos[0]][pos[1]+1])+1)
                return (pos[0], pos[1]+1), "E"
            else:
                return pos, ""
        except IndexError:
            return pos, ""    
            
We have identical checks for south, west and north as well.   

`step()` is the meat of this program. Whenever we move in the maze, there are two major factors that affect the order of spaces we check: our current direction, and which wall we are meant to be following. Depending on those two factors, we check each space in a certain order. If one of the combinations of spaces returns a valid new position, we return it as our next move.

    if (dirn == "E" and side == "R") or (dirn == "W" and side == "L"):
        pos, dirn = check_south(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_east(pos)
            elif side == "L":
                pos, dirn = check_west(pos)
        if dirn == "":
            pos, dirn = check_north(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_west(pos)
            elif side == "L":
                pos, dirn = check_east(pos)
        return pos, dirn

The above block trips if we are moving east following the right wall, or moving west following the left wall. There are three other structurally identical blocks which check all six other movement combinations in pairs.

We find the starting character of the maze and use it to set our starting direction.

    for i in range(height):
        for j in range(width):

            curr = maze[i][j]

            if curr in "><^v":
                pos = (i, j)
                if curr == ">":
                    dirn = "E"
                elif curr == "<":
                    dirn = "W"
                elif curr == "^":
                    dirn = "N"
                elif curr == "v":
                    dirn = "S"
                maze[i][j] = "0"

We store the starting position so that we know when to break our loop, then take one step forward so that we don't trigger the break condition immediately.
 
    starting_pos = pos
    pos, dirn = step(pos, dirn)

    while pos != starting_pos:
        pos, dirn = step(pos, dirn)

When we reach the starting point again, the traversal is finished. We print the updated maze to reflect the results of the traversal.

    for line in maze:
        for char in line:
            print(char, end="")
        print("")                
        
### Original Codingame Problem

https://www.codingame.com/training/easy/detective-pikaptcha-ep2
