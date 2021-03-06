# Information for "Power of Thor - Ep. 1"

### Rules and Implementation

The objective of this game is fairly straightforward. Thor starts on a map that is 18 tiles tall and 40 tiles high. He has a start
position, given by `(initial_tx, initial_ty)`, and he has to make it to a finishing point given by `(light_x, light_y)` in the given
number of turns. The game ends in a fail state if Thor wanders off the edge of the map, or if he does not make it to the light in time;
the game ends in a win state if he reaches the light with at least 0 turns remaining.

For each turn, the player outputs a direction they want Thor to move by printing a string to the console: `"N"`, `"NW"`, 
`"S"`, `"SE"` and so on. I opted to use a series of conditionals and for loops to accomplish this, as Thor could start in any direction
relative to the position of the light. Essentially, I'd calculate the Manhattan distance to the point (total units along `x` plus total
units along `y`), then use that information to determine which axis I was closer to the light on. From here, I'd move on a diagonal
to cover the shorter distance, while also covering a portion of the longer distance. Following this, I'd simply move on a vertical
or horizontal to cover the remaining portion of the longer distance, finishing the game.

I believe this is optimal input for any given test case. In fact, one of the test cases requries optimal input - I'll draw that case out 
along with a couple others to demonstrate.

### Example Test Cases

In all cases, Thor starts on the black dot and ends on the red dot. The blue line is the path taken between the two.

**Straight Line**

![](images/thor_straight.png)

This one is straightforward (pun intended.) Thor moves directly easy for 26 turns. 

**Easy Angle**

![](images/thor_easy.png)

This one is interesting in that "angle" is a misnomer here. The path shown here is optimal, but the test case input allows Thor to make enough moves that he could technically go straight down, then straight over, and still make it on time.

**Optimal Angle** 

![](images/thor_optimal.png)

This test case requires optimal movement. Thor moves on a diagonal to cover as much distance as possible, then moves horizontally to cover the remaining distance. 

### Original Codingame Problem

https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
