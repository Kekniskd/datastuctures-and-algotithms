def find_runner_up(arr: list) -> int:
    # Initialize variables to store the largest and second largest elements
    largest = second_largest = float('-inf')

    # Iterate through the array
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


array = [2, 3, 6, 6, 5]
array = [1, -1, -2, -1]
print(find_runner_up(array))
