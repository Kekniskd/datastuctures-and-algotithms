def linear_search(list: list, target: int) -> int:
    """
    Returns the index position of target if found, else returns None
    """
    for index, item in enumerate(list):
        print(f"{index}: {item}")
        if item == target:
            return index
    return None


def verify(index: int) -> str:
    if index:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [num for num in range(1,11)]
print(numbers)

result = linear_search(numbers, 10)
verify(result)