from test_utils import test_sort_function

def bubble_sort(elements: list) -> list:
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

    return elements


if __name__ == '__main__':
    test_sort_function(size_of_sample_set=10, sort_func=bubble_sort)
    test_sort_function(size_of_sample_set=5000, sort_func=bubble_sort)
    test_sort_function(size_of_sample_set=10000, sort_func=bubble_sort)
    test_sort_function(size_of_sample_set=20000, sort_func=bubble_sort)
    # really slow from here
    test_sort_function(size_of_sample_set=50000, sort_func=bubble_sort)
    