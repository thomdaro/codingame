# Information for "Graffiti on the Fence"

### Introduction and Example

The premise of this problem is as follows: you're hired to paint a fence, but you don't want to go through the effort yourself, so you hire a number of people to paint many sections of the fence. Unfortunately, you're also not very good at project management, so you don't give your workers any direction as to which parts of the fence to paint. They each choose a random interval to paint and report back to you with their choice. Given a list of reports of which parts of the fence are painted, you want to find out which parts are _not_ painted.

Say we have a fence 10 units long, and there are two intervals painted: 1 - 4, and 5 - 6. So our fence looks like this, with exclamation points denoting the ends of painted sections:

       !--------!  !--!
    +--+--+--+--+--+--+--+--+--+--+
    0  1  2  3  4  5  6  7  8  9  10
    
We can clearly see from this diagram that sections 0 - 1, 4 - 5, and 6 - 10 are unpainted. So how can we infer that simply from looking at the data, rather than an human-intuitive visual diagram? We may be tempted to use arrays for this, marking the sections that have been painted and traversing the array afterwards. Some of the test cases, however, have fences that are 2,000,000,000 units long, and we are limited to 100 total reports at most, meaning that an array of every position would use 2 GB of memory to track relatively little data. Therefore, it would be best to find a solution that does not involve using such a large, potentially inefficient array.

### I/O Format

#### Input

* __Line 1:__ An integer `L`, the length of the fence in meters.
* __Line 2:__ An integer `N`, the total number of reports received.
* __Next `N` Lines:__ The reports, each consisting of a `start` and `end` integer.

    [EXAMPLE]
    10
    2
    1 4
    5 6

#### Output

A list of unpainted sections in the same format as the reports, sorted in ascending order by `start`.
If there are no unpainted sections, print `All painted` instead.

    [EXAMPLE]
    0 1
    4 5
    6 10

### Code Walkthrough

Input processing is standard. We read in `l` and `n`, then read all reports into a list for processing.

    l = int(input())
    n = int(input())
    reports = []

    for i in range(n):
        st, ed = [int(j) for j in input().split()]
        reports.append([st, ed])

We sort `reports` by their start time, because we want to track where painted sections overlap. `cons` is short for "consolidated" here, and it refers to the fact that adjacent reports with overlapping end and start times will be consolidated or merged together in this list. Once we have a list of all painted sections sans overlap, we can easily determine which sections are unpainted. We'll start by simply copying over the first report, as this is the report with the earliest start time and needs no alteration.

    reports.sort(key = lambda x: x[0])
    cons = [reports[0].copy()]
    
`curr_ed` is the end of the current consolidated report. `reports[i][0]` is the start of the next report in the sorted report sequence. Therefore, if the start of the next report is behind or at the end of the consolidated interval, we change its endpoint to the maximum of the current end and the end of the next given report. Otherwise, we start a new consolidated record. We can use `-1` as the index for our current consolidated record, as we only need to modify the last record in the list if we're moving down the reports sequentially by start time.
    
    for i in range(1, n):
        curr_ed = cons[curr][1]
        if reports[i][0] <= curr_ed:
            cons[curr][1] = max(curr_ed, reports[i][1])
        else:
            cons.append(reports[i])
         
`answers` keeps track of all unpainted intervals, i.e. the gaps between consolidated reports. If the start of the first report is after the start of the fence itself, then there is an untracked, unpainted gap. We add it in first if this is the case.
         
    first_st = cons[0][0]
    answers = ["0 " + str(first_st)] if first_st > 0 else []
    
Next, we add in the gaps between consolidated records.
    
    for i in range(len(cons)-1):
        answers.append(str(cons[i][1]) + " " + str(cons[i+1][0]))  
 
And finally, we add in the end gap, if there is a space between the end of the last record and the end of the fence.
 
    last_ed = cons[len(cons)-1][1]
    if last_ed < l:
        answers.append(str(last_ed) + " " + str(l))
        
All that's left is to indicate which intervals are unpainted, if any. Intervals are already sorted in ascending order, so no further sorting is necessary.

    if answers == []:
        print("All painted")
    else:
        for answer in answers:
            print(answer)
            
### Original Codingame Problem

https://www.codingame.com/training/easy/graffiti-on-the-fence
