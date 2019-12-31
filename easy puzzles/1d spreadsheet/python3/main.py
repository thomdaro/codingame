import sys
import math

n = int(input())
inputs = []

for i in range(n):
    
    operation, arg_1, arg_2 = input().split()
    inputs.append((operation, arg_1, arg_2))

# list to keep track of results of previous cells
# (optimizes especially deep recursion)
results = [None for _ in range(len(inputs))]

# main recursive method
def process(index, op, a1, a2):
    
    a1_ref = -1
    a2_ref = -1
    
    # if a1 has a reference, grab it
    if a1[0] == '$':
        a1_ref = int(a1[1:])
    else:
        a1 = int(a1)
    
    # if the reference is not the default value
    if a1_ref >= 0:
        # if we haven't already solved the cell
        if results[a1_ref] == None:
            # process this cell
            rec_op = inputs[a1_ref][0]
            rec_a1 = inputs[a1_ref][1]
            rec_a2 = inputs[a1_ref][2]
            a1 = process(a1_ref, rec_op, rec_a1, rec_a2)
        else:
            # otherwise, grab the already-computed result
            a1 = results[a1_ref]
        
    # same process for a2
    if a2[0] == '$':
        a2_ref = int(a2[1:])
    # add addtl check for blank a2 (used for VALUE cells)
    elif a2[0] != '_':
        a2 = int(a2)
    
    if a2_ref >= 0:
        if results[a2_ref] == None:
            rec_op = inputs[a2_ref][0]
            rec_a1 = inputs[a2_ref][1]
            rec_a2 = inputs[a2_ref][2]
            a2 = process(a2_ref, rec_op, rec_a1, rec_a2)
        else:
            a2 = results[a2_ref]
        
    # by this point, both a1 and a2 are guaranteed to be integers
    if op == "VALUE":
        r = a1
    elif op == "ADD":
        r = a1 + a2
    elif op == "SUB":
        r = a1 - a2
    elif op == "MULT":
        r = a1 * a2
        
    # store result of this cell in the results array for future use
    results[index] = r
    # return the computed value and move up the stack
    return r

for i in range(n):
    
    operation = inputs[i][0]
    arg_1 = inputs[i][1]
    arg_2 = inputs[i][2]
    
    # do recursive process for all cells
    results[i] = process(i, operation, arg_1, arg_2)
    
for i in range(n):
    print(str(results[i]))