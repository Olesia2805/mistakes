"""
def find_max():
    numbers = input("Enter numbers separated by spaces: ")
    max_number = max(numbers)
    print("Maximum number:", max_number)

find_max()


def find_max():
    numbers = input("Enter numbers separated by spaces: ")
    data = [num for num in numbers.split(' ')]
    max_number = max(data)
    print("Maximum number:", max_number)

find_max()
