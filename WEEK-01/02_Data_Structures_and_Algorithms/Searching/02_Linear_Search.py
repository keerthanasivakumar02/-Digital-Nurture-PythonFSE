# Linear Search Example

def linear_search(numbers, target):

    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


numbers = [15, 25, 35, 45, 55]
target = 45

result = linear_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print("Element not found")