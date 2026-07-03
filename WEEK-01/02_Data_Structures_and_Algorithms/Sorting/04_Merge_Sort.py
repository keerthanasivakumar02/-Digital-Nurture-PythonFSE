# Merge Sort Example

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)

    return merged


numbers = [50, 20, 40, 10, 30]

print("Sorted Array:", merge_sort(numbers))