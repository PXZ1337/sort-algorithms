from test_utils import test_sort_function

def insertion_sort(elements: list) -> list:
    s, c = 0, 0

    for i, v in enumerate(range(1,len(elements)-1)):
        j = i
        c += 1
        while (j > 0 and elements[j-1] > v):
            elements[j], elements[j-1], j = elements[j-1], elements[j], j-1
            s += 1

    print(f"--- Compares / Swaps: {c} / {s}")

    return elements

if __name__ == '__main__':
    test_sort_function(size_of_sample_set=10, sort_func=insertion_sort)
    test_sort_function(size_of_sample_set=5000, sort_func=insertion_sort)
    test_sort_function(size_of_sample_set=10000, sort_func=insertion_sort)
    test_sort_function(size_of_sample_set=20000, sort_func=insertion_sort)
    # really slow from here
    test_sort_function(size_of_sample_set=50000, sort_func=insertion_sort)