def max_alternate_subsequence(arr):
    if not arr:
        return 0

    # Initialize variables to keep track of the length of the alternating subsequence
    max_len = 0  # Maximum length of alternating subsequence
    current_len = 1  # Length of current alternating subsequence

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            # If the current element is different from the previous one, it's part of the alternating subsequence
            current_len += 1
        else:
            # If the current element is the same as the previous one, the alternating subsequence ends here
            max_len = max(max_len, current_len)  # Update max_len if necessary
            current_len = 1  # Reset current_len

    # Update max_len in case the last element extends the alternating subsequence
    max_len = max(max_len, current_len)

    return max_len


# Example usage:
arr = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
print(max_alternate_subsequence(arr))
