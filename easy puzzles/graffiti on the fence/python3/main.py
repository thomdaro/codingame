import sys
import math

l = int(input())
n = int(input())
reports = []

for i in range(n):
    st, ed = [int(j) for j in input().split()]
    reports.append([st, ed])

# sort all reports by start, since we want to find overlap
reports.sort(key = lambda x: x[0])
# 'cons' is short for 'consolidated', and will hold the
# intersection of all painted sections (i.e. no overlap)
cons = [reports[0].copy()]

# skip first record since this one is already in cons
for i in range(1, n):
    curr_ed = cons[-1][1]
    # if the start of the current record is behind the consolidated end
    if reports[i][0] <= curr_ed:
        # change the end of cons[curr] to the furthest endpoint
        cons[-1][1] = max(curr_ed, reports[i][1])
    # if we have no overlap
    else:
        # start consolidating a new record
        cons.append(reports[i])
    
# add an unpainted section from the start to the first painted section if needed
first_st = cons[0][0]
answers = ["0 " + str(first_st)] if first_st > 0 else []

# add the gaps between consolidated records
for i in range(len(cons)-1):
    answers.append(str(cons[i][1]) + " " + str(cons[i+1][0]))
    
# add the end gap if needed
last_ed = cons[len(cons)-1][1]
if last_ed < l:
    answers.append(str(last_ed) + " " + str(l))

if answers == []:
    print("All painted")
else:
    for answer in answers:
        print(answer)
