# Sorting Algorithms <!-- omit in toc -->

This repository contains a collection of well known sorting algorithms.

The implementations are written with the programming language Python and tested against the build-in `sort()` function. The metrics could be used to compare the performance between the different kinds of algorithms on different sizes of input data.

## Metrics <!-- omit in toc -->

- Execution time of the algorithm in seconds
- Number of comparisons
- Number of swaps

## Table of contents <!-- omit in toc -->

- [Bubblesort](#bubblesort)
  - [Performance (BS)](#performance-bs)
- [Selectionsort](#selectionsort)
  - [Performance (SS)](#performance-ss)
- [Insertionsort](#insertionsort)
  - [Performance (IS)](#performance-is)

## Bubblesort

Simple in-place sorting algorithm which iterates over each element in the list and compares the current with the next element.

Performs poorly on big unsorted lists and is primary used as and educational tool.

### Performance (BS)

| Case     | Time complexity         |
|----------|-------------------------|
| Worst       | O(n^2) comparisons   |
| performance | O(n^2) swaps         |
| Best        | O(n) comparisons     |
| performance | O(1) swaps           |
| Average     | O(n^2) comparisons   |
| performance | O(n^2) swaps         |

Run [bubble_sort.py](src/bubble_sort.py).

The script will excute the sorting_algorithm multiple times with an random generated dataset which is increased in size every new iteration. After the execution an assert function is checking the result for consistency.

## Selectionsort

Simple in-place sorting algorithm which sorts list's by creating a sorted sublist. This sorted list is filled by finding the smallest element each iteration in the unsorted list and put them at the end of the sorted list.

### Performance (SS)

| Case     | Time complexity      |
|----------|----------------------|
| Worst       | O(n^2) comparisons|
| performance | O(n) swaps        |
| Best        | O(n^2) comparisons|
| performance | O(1) swaps        |
| Average     | O(n^2) comparisons|
| performance | O(n) swaps        |

Run [selection_sort.py](src/selection_sort.py).

## Insertionsort

In-place sorting algorithm that is much less efficient than quicksort, heapsort or mergesort but gives advantages against bubblesort and insertion sort because of the adaptive behavoir on already substantially sorted lists.

It iterates over the list, consumes one element each iteration and move's that element to the correct position in the list.

### Performance (IS)

| Case     | Time complexity      |
|----------|----------------------|
| Worst       | O(n^2) comparisons|
| performance | O(n^2) swaps        |
| Best        | O(n) comparisons|
| performance | O(1) swaps        |
| Average     | O(n^2) comparisons|
| performance | O(n^2) swaps        |

Run [insertion_sort.py](src/insertion_sort.py).

