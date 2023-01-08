def slowsort(arr):
    """slowsort"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = slowsort(arr[:mid])
    right = slowsort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """merge slowsort"""
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
