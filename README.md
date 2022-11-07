# Sorting Algorithms

This repository contains a collection of well known computer science sorting algorithms.

The implementations are written with the programming language Python and tested against the build-in `sort()` function.

## Metrics

- Execution time of the algorithm in seconds
- Number of comparisons
- Number of swaps

## Bubblesort

Simple in-place sorting algorithm which iterates over each element in the list and compares the current with the next element.

Performs poorly on big unsorted lists and is primary used as and educational tool.

### Performance

| Case     | Time complexity         |
|----------|-------------------------|
| Worst       | O(n^2) comparisons   |
| performance | O(n^2) swaps         |
| Best        | O(n) comparisons     |
| performance | O(1) swaps           |
| Average     | O(n^2) comparisons   |
| performance | O(n^2) swaps         |

Run [bubble_sort.py](bubble_sort.py).

The script will excute the sorting_algorithm multiple times with an random generated dataset which is increased in size every new iteration. After the execution an assert function is checking the result for consistency.

## Selectionsort

Simple in-place sorting algorithm which sorts list's by creating a sorted sublist. This sorted list is filled by finding the smallest element each iteration in the unsorted list and put them at the end of the sorted list.

### Performance

| Case     | Time complexity      |
|----------|----------------------|
| Worst       | O(n^2) comparisons|
| performance | O(n) swaps        |
| Best        | O(n^2) comparisons|
| performance | O(1) swaps        |
| Average     | O(n^2) comparisons|
| performance | O(n) swaps        |

Run [selection_sort.py](selection_sort.py).
