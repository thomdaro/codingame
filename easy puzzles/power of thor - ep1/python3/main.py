import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    x_diff = abs(initial_tx - light_x)
    y_diff = abs(initial_ty - light_y)
    shorter_dist = min(x_diff, y_diff)
    
    if light_x <= initial_tx and light_y <= initial_ty:
        for _ in range(shorter_dist):
            print("NW")
        for _ in range(x_diff - y_diff):
            print("W")
        for _ in range(y_diff - x_diff):
            print("N")
    elif light_x >= initial_tx and light_y <= initial_ty:
        for _ in range(shorter_dist):
            print("NE")
        for _ in range(x_diff - y_diff):
            print("E")
        for _ in range(y_diff - x_diff):
            print("N")
    elif light_x <= initial_tx and light_y >= initial_ty:
        for _ in range(shorter_dist):
            print("SW")
        for _ in range(x_diff - y_diff):
            print("W")
        for _ in range(y_diff - x_diff):
            print("S")
    elif light_x >= initial_tx and light_y >= initial_ty:
        for _ in range(shorter_dist):
            print("SE")
        for _ in range(x_diff - y_diff):
            print("E")
        for _ in range(y_diff - x_diff):
            print("S")