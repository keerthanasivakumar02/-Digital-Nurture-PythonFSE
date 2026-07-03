# Bubble Sort Example

numbers = [45, 12, 78, 23, 9]

n = len(numbers)

for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted Array:", numbers)