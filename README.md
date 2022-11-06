# Sorting Algorithms

Collection of sorting algorithm implementations, including testing and performance comparison.  

## Bubblesort

Simple sorting algorithm which iterates over each element in the list and compares the current with the next element. 

Performs poorly on big unsorted lists and is primary used as and educational tool.

| Case     | Time complexity      |
|----------|----------------------|
| Best     | O on pre sorted list |
| Worst    | O(n^2)               |
| Average  | O(n^2)               |


### Description

Run [bubble_sort.py](bubble_sort.py).

The script will excute the sorting_algorithm multiple times with an random generated dataset which is increased in size every new iteration. After the execution an assert function is checking the result for consistency.

### Metrics

- Execution time in seconds
- Number of comparisons
- Number of switches