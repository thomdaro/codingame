# Information for "Rectangle Partition"

### Introduction and Example

We start with a rectangle of width `w` and height `h`. We're given a series of integers between 0 and `w`, and another series between 0 and `h`. For each integer in these series, we draw a perpendicular line down the respective side, dividing the rectangle into many smaller rectangles. The question we wish to answer is: given this partitioned rectangle, how many internally formed rectangles (including all combinations of rectangles) are squares?

Here's an example from the brief on Codingame.

    w = 10
    h = 5
    measurements on x-axis: 2, 5
    measurements on y-axis: 3

       ___2______5__________ 
      |   |      |          |
      |   |      |          |
     3|___|______|__________|
      |   |      |          |
      |___|______|__________|

    Number of squares in sub-rectangles = 4 (one 2x2, one 3x3, two 5x5)
    
### Input Format

A typical test case input looks like this.

* __Line 1__: Four integers. `w` for the width of the rectangle, `h` for the height, `countX` for the number of partitions along the X-axis and `countY` for the number of partitions along the Y-axis. Separated by commas.
* __Line 2__: `countX` integers indicating the X-axis partitions, sorted in ascending order.
* __Line 3__: `countY` integers indicating the Y-axis partitions, sorted in ascending order.

### Code Walkthrough

Before anything else, we need to process our input. `xs` and `ys` will be used to store the partition points. They are initialized with the left and top edge of the rectangle at `0`, so that we can calculate the distance between the edge and the first partition later.

    w, h, count_x, count_y = [int(i) for i in input().split()]
    xs = [0]
    ys = [0]
    
We populate `xs` and `ys` with the given partitions, then add the right and bottom edges at `w` and `h`, respectively.

    for i in input().split():
        x = int(i)
        xs.append(x)
    xs.append(w)

    for i in input().split():
        y = int(i)
        ys.append(y)
    ys.append(h)
    
We initialize two more lists to hold the differences between all pairs of `xs` and `ys`, without repeating calculations between pairs.

    x_diffs = []
    y_diffs = []

    for i in range(len(xs)-1):
        for j in range(i+1, len(xs)):
            x_diffs.append(xs[j]-xs[i])

    for i in range(len(ys)-1):
        for j in range(i+1, len(ys)):
            y_diffs.append(ys[j]-ys[i])
            
A square occurs when the distance between any two X-axis partitions equals the distance between any two Y-axis partitions. This checks for all unique pairs of equidistant X- and Y-axis partitions, then prints the total number as `squares`.             
            
    squares = 0

    for x_diff in x_diffs:
        squares += y_diffs.count(x_diff)

    print(str(squares))
    
### Original Codingame Problem

https://www.codingame.com/training/easy/rectangle-partition
