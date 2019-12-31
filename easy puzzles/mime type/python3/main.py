import sys
import math

n = int(input())
q = int(input())  
assoc_table = {} # use dictionary as a table

for i in range(n):
    ext, mt = input().split()
    assoc_table[ext.lower()] = mt # remove case comparison issues with lower()
        
for i in range(q):
    fname = input()
    # use lower() for comparison
    f_ext = fname[fname.rfind(".") + 1:].lower()
    # rfind returns -1 if not found so check to ensure fname has a '.'
    if "." in fname and f_ext in assoc_table:
        print(assoc_table[f_ext])
    else:
        print("UNKNOWN")