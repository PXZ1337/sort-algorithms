from test_utils import test_sort_function

def selection_sort(elements: list) -> list:
    s, c = 0, 0

    for (i,_) in enumerate(elements):
        min = i
        for (j,_) in enumerate(elements): 
            c += 1
            if (elements[j] < elements[min]):
                min = j

        if i != min:
            elements[i], elements[min] = elements[min], elements[i]
            s += 1

    print(f"--- Compares / Swaps: {c} / {s}")

    return elements

if __name__ == '__main__':
    test_sort_function(size_of_sample_set=10, sort_func=selection_sort)
    test_sort_function(size_of_sample_set=5000, sort_func=selection_sort)
    test_sort_function(size_of_sample_set=10000, sort_func=selection_sort)
    test_sort_function(size_of_sample_set=20000, sort_func=selection_sort)
    # really slow from here
    test_sort_function(size_of_sample_set=50000, sort_func=selection_sort)
     