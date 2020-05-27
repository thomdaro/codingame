# Information for "Lumen"

### Introduction and Example

This puzzle involves a room with a number of candles placed around a square room. Each candle has a base light level, and that light diffuses as it gets farther from the candle. Given a room and several candles of a particular light level in the room, we want to find all spaces in the room with zero light.

For each test case, we receive a map of the room, where `X` is an unoccupied tile and `C` denotes a candle. Maps look like this:

    X X X X X
    X C X X X
    X X X X X
    X X X X X
    X X X X X
    
Given that this candle has a base light level of 3, the light map looks like this.

    2 2 2 1 0
    2 3 2 1 0
    2 2 2 1 0
    1 1 1 1 0
    0 0 0 0 0
    
Where the space with the candle itself is the base level, all adjacent squares are one below, are squares adjacent to those are one below, and so on. We would return `9` in this case, as there are 9 spaces with no light.

### I/O Format

#### Input

* __Line 1:__ An integer `N`, indicating the length of one side of the room.
* __Line 2:__ An integer `L`, indicating the base light level of the candles.
* __Next `N` Lines:__ `N` characters, separated by spaces, indicating the layout of the room and its candle placements.

#### Output

An integer `n`, indicating the number of zero-light spaces in the room.

### Code Walkthrough

We need to transform the strings of the room layout into index-able lists, so we iterate over the strings, populating a list with `0` to indicate a floor tile and the base light level to indicate a candle. We also keep track of the positions of the candles for further processing.

    n = int(input())
    l = int(input())
    room = [[] for _ in range(n)]
    candle_psns = []

    for i in range(n):
        line = input()
        for j in range(n*2-1):
            char = line[j]
            if char != ' ':
                if char == "X":
                    room[i].append(0)
                elif char == "C":
                    room[i].append(l)
                    candle_psns.append((i, j // 2))
                
This essentially gives us our lightmap. For each candle, we check in a series of concentric circles around it. For each valid index we find, we assign the appropriate light level. If a space is touched by the light of multiple candles, it is added to the existing light level.

    for pos in candle_psns:
        for i in range(1,l):
            for j in range(-i,i+1):
                for k in range(-i,i+1):
                    try:
                        if pos[0]+j >= 0 and pos[1]+k >= 0 and math.sqrt(j**2 + k**2) >= i:
                            room[pos[0]+j][pos[1]+k] += l-i
                    except IndexError:
                        pass

Now that we've established which spaces are lit, we simply count up unlit spaces and print the final result.

    res = 0
    for line in room:
        for char in line:
            if char == 0:
                res += 1   
                
    print(str(res))
    
### Original Codingame Problem

https://www.codingame.com/training/easy/lumen
