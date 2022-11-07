import random
import time

def selection_sort(elements: list) -> list:
    start_time = time.time()
    s, c = 0, 0

    for (i,v) in enumerate(elements):
        min = i
        for (j,_) in enumerate(elements): 
            c += 1
            if (elements[j] < elements[min]):
                min = j

        if i != min:
            elements[i], elements[min] = elements[min], elements[i]
            s += 1

    print(f"--- Compares / Swaps: {c} / {s}")
    print("--- %s seconds ---" % (time.time() - start_time))

    return elements

def test_selection_sort(size_of_sample_set: int, verbose: bool = False):
    x, y = -size_of_sample_set, size_of_sample_set
    expectation = random.sample(range(x, y), size_of_sample_set)
    actual = selection_sort(expectation)
    
    if verbose:
        print(f"expectation: {expectation}, actual: {actual}")

    expectation.sort()

    assert actual == expectation


if __name__ == '__main__':
    test_selection_sort(10)
    test_selection_sort(5000)
    test_selection_sort(10000)
    test_selection_sort(20000)
    # really slow from here
    test_selection_sort(50000)
    