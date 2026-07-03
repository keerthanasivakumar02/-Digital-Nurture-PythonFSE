# Quick Sort Example

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    greater = []

    for num in arr[:-1]:
        if num <= pivot:
            smaller.append(num)
        else:
            greater.append(num)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


numbers = [25, 15, 35, 10, 5]

print("Sorted Array:", quick_sort(numbers))