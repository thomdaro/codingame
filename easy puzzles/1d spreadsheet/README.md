# Information for "1D Spreadsheet"

### Introduction

Input consists of a "one-dimensional" spreadsheet, essentially a list of cells given in the format `operation arg1 arg2`. There are four types of operations:

1. `VALUE`. The cell's value is `arg1`, and `arg2` is given as a `_`, as it is unused.
2. `ADD`. The cell's value is `arg1 + arg2`.
3. `SUB`. The cell's value is `arg1 - arg2`.
4. `MULT`. The cell's value is `arg1 x arg2`.

Additionally, arguments come in one of two flavors.

1. References, formatted as `$ref`, where `ref` is the index of the cell referenced. This reference is interpreted as the value of the cell it references. Cells are allowed to reference cells that come after them in the list.
2. Values. If the argument is a number, rather than a reference, it will have an integer in its place.

There are no cyclic references, i.e. cells that reference in a chain of any length back to themselves.

### Input Format and Example

* __Line 1:__ An integer `N` for the number of cells in the list.
* __Next `N` Lines:__ `operation arg1 arg2`, where the `operation` is one of the four listed above, and `args` are either a value, reference, or nothing (`_`).

A simple example is as follows.

    2
    VALUE 3 _
    ADD $0 4
    
We see that there are two cells in this list. Cell 0 is `VALUE 3 _`, therefore its value is `3`. Cell 1 is `ADD $0 4`, so we pull the value of Cell 0 and add `4`, giving us `7`. We then output the values of all cells in index order:

    3
    7
    
### Code Walkthrough

Input processing is fairly standard here. We read the cells into a list of tuples for easy indexing, then create an additional list of all solved cells and their results to reduce recursion calls.

    n = int(input())
    inputs = []

    for i in range(n):

        operation, arg_1, arg_2 = input().split()
        inputs.append((operation, arg_1, arg_2))
        
    results = [None for _ in range(len(inputs))]
    
We'll use a recursive, dynamic programming approach to solve this problem. `process` takes four arguments: the index of the current cell, along with that cell's operation and arguments. If the first argument is a reference, we grab that reference; otherwise we process the argument as an integer.
    
    def process(index, op, a1, a2):
    
        a1_ref = -1
        a2_ref = -1

        if a1[0] == '$':
            a1_ref = int(a1[1:])
        else:
            a1 = int(a1)
     
If we find a reference in the first argument, and that reference has not been solved yet, then we make a recursive call on that cell. If the results array contains a value for that cell, we pull it.
     
    if a1_ref >= 0:
        if results[a1_ref] == None:
            rec_op = inputs[a1_ref][0]
            rec_a1 = inputs[a1_ref][1]
            rec_a2 = inputs[a1_ref][2]
            a1 = process(a1_ref, rec_op, rec_a1, rec_a2)
        else:
            a1 = results[a1_ref]      
            
We perform the exact same process for `arg2` – the code is identical save for the argument referenced.

Having computed both `arg1` and `arg2` for this cell, we use some simple logic to perform the cell's given `operation`. We then store the result of that operation in the results array for future calls, and return the final value so that it may be used in calculations above it in the stack if necessary.

    if op == "VALUE":
        r = a1
    elif op == "ADD":
        r = a1 + a2
    elif op == "SUB":
        r = a1 - a2
    elif op == "MULT":
        r = a1 * a2
        
    results[index] = r
    return r
  
This concludes our recursive method for computing cell values. All that remains is to call it on all cells in the spreadsheet sequentially. Each cell is only computed once, so this process runs in O(_n_) assuming that lookups are O(1). We then print the results array line-by-line to get our final output.
  
    for i in range(n):

        operation = inputs[i][0]
        arg_1 = inputs[i][1]
        arg_2 = inputs[i][2]

        # do recursive process for all cells
        results[i] = process(i, operation, arg_1, arg_2)

    for i in range(n):
        print(str(results[i]))    
        
### Original Codingame Problem

https://www.codingame.com/training/easy/1d-spreadsheet
