from test_utils import test_sort_function

def quick_sort(elements: list) -> list:
    if len(elements) <= 1: 
        return elements
    
    left, right = [], []
    pivot = len(elements) // 2
    
    for i, v in enumerate(elements):
        if (i == pivot): 
            continue
        left.append(v) if (v <= elements[pivot]) else right.append(v)

    result: list = []
    result.extend(quick_sort(left))
    result.append(elements[pivot])
    result.extend(quick_sort(right))

    return result


if __name__ == '__main__':
    test_sort_function(size_of_sample_set=50000, sort_func=quick_sort)
    test_sort_function(size_of_sample_set=100000, sort_func=quick_sort)
    test_sort_function(size_of_sample_set=1000000, sort_func=quick_sort)