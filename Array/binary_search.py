def binary_search(list: list, target: int) -> int:
    """
    Returns the index position of target if found, else returns None through Binary-search algorithm
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        print(f"{midpoint}: {list[midpoint]}")
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index: int) -> str:
    if index:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [num for num in range(1,101)]
# print(numbers)

result = binary_search(numbers, 101)
verify(result)