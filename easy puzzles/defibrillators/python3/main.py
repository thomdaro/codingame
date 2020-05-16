import sys
import math

# replace ',' with '.' and convert to float for processing
lon = math.radians(float(input().replace(',', '.')))
lat = math.radians(float(input().replace(',', '.')))
n = int(input())

# make closest distance the maximum possible under given formula
closest_defib_dist = math.ceil(math.pi * 6371)
closest_defib = ""

for i in range(n):
    defib = input().split(';')
    # convert to string for replacement, then back to float
    defib_long = math.radians(float(str(defib[4]).replace(',', '.')))
    defib_lat  = math.radians(float(str(defib[5]).replace(',', '.')))
    # apply formulas from here, check for closer distance and assign
    x = (defib_long - lon) * math.cos((lat + defib_lat) / 2)
    y = defib_lat - lat
    d = math.sqrt(x**2 + y**2) * 6371
    
    if d < closest_defib_dist:
        closest_defib_dist = d
        closest_defib = defib[1]

print(closest_defib)