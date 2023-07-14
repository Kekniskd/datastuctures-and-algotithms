def rec_binary_search(list: list, target: int) -> bool:
    """
    Returns the index position of target if found, else returns None through recursive Binary-search algorithm
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return rec_binary_search(list[midpoint+1:], target)
            else:
                return rec_binary_search(list[:midpoint], target)


def verify(result):
    print(f"Target found: {result}")


numbers = [num for num in range(1,101)]
# print(numbers)

result = rec_binary_search(numbers, 50)
verify(result)