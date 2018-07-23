def binary_search(list_of_numbers, number):
    low = 0
    high = len(list_of_numbers) - 1
    while low <= high:
        middle = (low + high) // 2
        if list_of_numbers[middle] > number:
            high = middle - 1
        elif list_of_numbers[middle] < number:
            low = middle + 1
        else:
            return middle
    raise ValueError("Value not found.")
