"""
def find_max(lst):
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value

numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print("Maximum list element:", find_max(numbers))
"""

def find_max(lst):
    try:
        max_value = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        return max_value
    except:
        ValueError

def test_find_max():
    # Test 1: Svichaynyy fall
    numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
    assert find_max(numbers) == 12, "Test 1 failed"

    # Test 2: All negative numbers
    numbers = [-5, -9, -3, -8, -4]
    assert find_max(numbers) == -3, "Test 2 failed"

    # Test 3: One element in the list
    numbers = [7]
    assert find_max(numbers) == 7, "Test 3 failed"

    # Test 4: Empty list
    numbers = []
    assert find_max(numbers) == None, "Test 4 failed"

    # Test 5: All the new elements
    numbers = [4, 4, 4, 4]
    assert find_max(numbers) == 4, "Test 5 failed"

    # Test 6: Floating points
    numbers = [1.5, 2.3, 0.7, 3.9, 2.2]
    assert find_max(numbers) == 3.9, "Test 6 failed"

    # Test 7: Mixed list with integers and floating points
    numbers = [1, 2.5, 3, 0.5, 4.5, 3.5]
    assert find_max(numbers) == 4.5, "Test 7 failed"

    print("All tests passed")

# Running tests
test_find_max()