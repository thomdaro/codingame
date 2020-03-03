# Information for "Temperatures"

### Rules and Implementation

Given a number of temperatures to analyze (`N`) and a string of temperatures separated by commas, determine the temperature that's closest to zero and output it. `N` must be between 0 and 9999 inclusive, and if no temperatures are shown, the "closest temperature" is zero. When a positive and a negative temperature are equally close to 0, choose the positive one.

Essentially, this is done by splitting the input to analyze each temperature individually, then comparing its absolute value with the current closest temp. There are two potential cases in which the closest temp is updated - either (a) the absolute value is lower or (b) the absolute value is the same, but the new temperature is positive.

### Example Test Cases

**Simple**

Input: 1 -2 -8 4 5
Expected Output: 1

This one is fairly straightfoward. 1 is the closest temperature here, and because it's the first one, our output doesn't change after the first analysis.

**Choose**

Input: 42 -5 12 21 5 24
Expected Output: 5

This one makes use of the "equal absolute value and positive" condition, so while -5 is closest, 5 trips this condition and becomes our output.

**Complex**

Input: -5 -4 -2 12 -40 4 2 18 11 5
Expected Output: 2

This makes use of the same condition, but it hides the desired output in the middle of the input.

### Original Codingame Problem

https://www.codingame.com/ide/puzzle/temperatures
