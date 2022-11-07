import random
import time

def bubble_sort(elements: list) -> list:
    start_time = time.time()
    s, c = 0, 0

    for (i,_) in enumerate(elements):
        swapped = False
        for (j,_) in enumerate(elements[:-(i+1)]): 
            c += 1
            if (elements[j] > elements[j+1]):
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
                s += 1
        if not swapped:
            break

    print(f"--- Compares / Swaps: {c} / {s}")
    print("--- %s seconds ---" % (time.time() - start_time))

    return elements

def test_bubble_sort(size_of_sample_set: int):
    x, y = -size_of_sample_set, size_of_sample_set
    expectation = random.sample(range(x, y), size_of_sample_set)
    actual = bubble_sort(expectation)
    expectation.sort()

    assert actual == expectation


if __name__ == '__main__':
    test_bubble_sort(10)
    test_bubble_sort(5000)
    test_bubble_sort(10000)
    test_bubble_sort(20000)
    # really slow from here
    test_bubble_sort(50000)
    