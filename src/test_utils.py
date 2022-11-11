import random, time
from typing import Callable

def test_sort_function(size_of_sample_set: int, sort_func: Callable):
    x, y = -size_of_sample_set, size_of_sample_set
    expectation = random.sample(range(x, y), size_of_sample_set)

    start_time = time.time()
    actual = sort_func(expectation)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    print(f"---expectation: {expectation[:10]}..., actual: {actual[:10]}...")

    expectation.sort()

    assert actual == expectation