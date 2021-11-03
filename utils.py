def find_max(numbers):
    largest_number = numbers[0]
    for item in numbers:
        if item > largest_number:
            largest_number = item
    return largest_number


def test():
    return 1
