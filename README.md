# Sorting Algorithms <!-- omit in toc -->

This repository contains a collection of well known sorting algorithms.

The implementations are written with the programming language Python and tested against the build-in `sort()` function. The metrics could be used to compare the performance between the different kinds of algorithms on different sizes of input data.

## Metrics <!-- omit in toc -->

- Execution time of the algorithm in seconds
- Number of comparisons
- Number of swaps

## Badges explanations <!-- omit in toc -->

- **Fast:** recommended to use for bigger lists
- **Adaptive:** efficient for data sets that are already substantially sorted
- **Stable:** does not change the relative order of elements with equal keys
- **In-place:** only requires a constant amount O(1) of additional memory space
- **Devide-and-Conquer:** Algorithm design pattern used to break down problems to multiple smaller problems.

## Table of contents <!-- omit in toc -->

- [Bubblesort](#bubblesort)
- [Selectionsort](#selectionsort)
- [Insertionsort](#insertionsort)
- [Quicksort](#quicksort)

## Bubblesort

[![In-place](https://img.shields.io/badge/in_place-yes.svg)](https://shields.io/)
[![Stable](https://img.shields.io/badge/stable-yes.svg)](https://shields.io/)
[![Fast](https://img.shields.io/badge/fast-red.svg)](https://shields.io/)

Simple in-place sorting algorithm which iterates over each element in the list and compares the current with the next element.

Performs poorly on big unsorted lists and is primary used as and educational tool.

### Time-Complexity (BS) <!-- omit in toc -->

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

[![In-place](https://img.shields.io/badge/in_place-yes.svg)](https://shields.io/)
[![Stable](https://img.shields.io/badge/stable-yes.svg)](https://shields.io/)
[![Fast](https://img.shields.io/badge/fast-red.svg)](https://shields.io/)

Simple in-place sorting algorithm which sorts list's by creating a sorted sublist. This sorted list is filled by finding the smallest element each iteration in the unsorted list and put them at the end of the sorted list.

### Time-Complexity (SS) <!-- omit in toc -->

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

[![In-place](https://img.shields.io/badge/in_place-yes.svg)](https://shields.io/)
[![Stable](https://img.shields.io/badge/stable-yes.svg)](https://shields.io/)
[![Adaptive](https://img.shields.io/badge/adaptive-yes.svg)](https://shields.io/)
[![Fast](https://img.shields.io/badge/fast-red.svg)](https://shields.io/)

In-place sorting algorithm that is much less efficient than quicksort, heapsort or mergesort but gives advantages against bubblesort and insertion sort because of the adaptive behavoir on already substantially sorted lists.

It iterates over the list, consumes one element each iteration and move's that element to the correct position in the list.

### Time-Complexity (IS) <!-- omit in toc -->

| Case     | Time complexity      |
|----------|----------------------|
| Worst       | O(n^2) comparisons|
| performance | O(n^2) swaps        |
| Best        | O(n) comparisons|
| performance | O(1) swaps        |
| Average     | O(n^2) comparisons|
| performance | O(n^2) swaps        |

Run [insertion_sort.py](src/insertion_sort.py).

## Quicksort

[![Devide and Conquer](https://img.shields.io/badge/devide_and_conquer-yes.svg)](https://shields.io/)
[![Fast](https://img.shields.io/badge/fast-yes.svg)](https://shields.io/)
[![In-place](https://img.shields.io/badge/in_place-yes.svg)](https://shields.io/)
[![Stable](https://img.shields.io/badge/stable-red.svg)](https://shields.io/)

Commonly used in-place sorting algorithm which could be faster than mergesort and about 2-3 times faster than heapsort. Quicksort uses the concept of devide-and-conquer to devide a list into 2 sub lists according to wheter the elements are less or greater than the pivot element.

### Time-Complexity (QS) <!-- omit in toc -->

| Case     | Time complexity      |
|----------|----------------------|
| Worst       | O(n^2)            |
| Best        | O(n log(n))       |
| Average     | O(n log(n))       |

Run [quick_sort.py](src/quick_sort.py).
