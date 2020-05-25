import sys
import math

width, height = [int(i) for i in input().split()]
maze = [[] for _ in range(height)]
pos = (-1, -1)
dirn = ""

for i in range(height):
    line = input()
    for char in line:
        maze[i].append(char)
    
side = input() 

def check_east(pos):
    try:
        if maze[pos[0]][pos[1]+1] != "#":
            maze[pos[0]][pos[1]+1] = str(int(maze[pos[0]][pos[1]+1])+1)
            return (pos[0], pos[1]+1), "E"
        else:
            return pos, ""
    except IndexError:
        return pos, ""
            
def check_west(pos):
    try:
        if maze[pos[0]][pos[1]-1] != "#" and pos[1]-1 >= 0:
            maze[pos[0]][pos[1]-1] = str(int(maze[pos[0]][pos[1]-1])+1)
            return (pos[0], pos[1]-1), "W"
        else:
            return pos, ""
    except IndexError:
        return pos, ""

def check_north(pos):
    try:
        if maze[pos[0]-1][pos[1]] != "#" and pos[0]-1 >= 0:
            maze[pos[0]-1][pos[1]] = str(int(maze[pos[0]-1][pos[1]])+1)
            return (pos[0]-1, pos[1]), "N"
        else:
            return pos, ""
    except IndexError:
        return pos, ""
            
def check_south(pos):
    try:
        if maze[pos[0]+1][pos[1]] != "#":
            maze[pos[0]+1][pos[1]] = str(int(maze[pos[0]+1][pos[1]])+1)
            return (pos[0]+1, pos[1]), "S"
        else:
            return pos, ""
    except IndexError:
        return pos, ""
            
def step(pos, dirn):
    
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
        
    if (dirn == "W" and side == "R") or (dirn == "E" and side == "L"):
        pos, dirn = check_north(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_west(pos)
            elif side == "L":
                pos, dirn = check_east(pos)
        if dirn == "":
            pos, dirn = check_south(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_east(pos)
            elif side == "L":
                pos, dirn = check_west(pos)
        return pos, dirn
        
    if (dirn == "N" and side == "R") or (dirn == "S" and side == "L"):
        pos, dirn = check_east(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_north(pos)
            elif side == "L":
                pos, dirn = check_south(pos)
        if dirn == "":
            pos, dirn = check_west(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_south(pos)
            elif side == "L":
                pos, dirn = check_north(pos)
        return pos, dirn
        
    if (dirn == "S" and side == "R") or (dirn == "N" and side == "L"):
        pos, dirn = check_west(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_south(pos)
            elif side == "L":
                pos, dirn = check_north(pos)
        if dirn == "":
            pos, dirn = check_east(pos)
        if dirn == "":
            if side == "R":
                pos, dirn = check_north(pos)
            elif side == "L":
                pos, dirn = check_south(pos)
        return pos, dirn
        

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

starting_pos = pos
pos, dirn = step(pos, dirn)

while pos != starting_pos:
    pos, dirn = step(pos, dirn)
    
for line in maze:
    for char in line:
        print(char, end="")
    print("")

# print(, file=sys.stderr)
