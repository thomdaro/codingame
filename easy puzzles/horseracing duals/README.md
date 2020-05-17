# Information for "Horse-racing Duals"

### Rules and Implementation

This is a simple problem, and I believe it serves as Codingame's introduction to algorithm design and understanding things like big-O time. We are given `N` integers and asked to return the smallest difference between any two integers in the set. This can be done in `O(N^2)` time with fairly small sets, where each element gets compared to every other element. Input sets in this problem, however can be up to 100,000 elements in size. This necessitates a more efficient algorithm, naturally. We can improve this algorithm by realizing that the smallest difference between any one element and the rest of the set would be between its adjacent elements in a sorted list.

If we sort the dataset first, this reduces the time complexity to `O(N log N)`, because we can simply compare adjacent elements in a sorted list to find the smallest difference between two elements, which runs in linear time. This allows us to process extremely large datasets fairly efficiently – enough that Codingame doesn't time out on the large case, anyway.

### Original Codingame Problem

https://www.codingame.com/training/easy/horse-racing-duals
