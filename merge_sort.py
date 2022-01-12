def merge_sort(list: list) -> None:
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Takes O(n log n) time 
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list: list) -> list:
    """
    Divides the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left: list, right:list) -> list:
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Takes overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify(list: list) -> bool:
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify(list[1:])


li = [100,4,55,8,9,1,6,7,54,84,76,12,48,64,34,38]
new_li = merge_sort(li)
print(new_li)
print(verify(li))
print(verify(new_li))