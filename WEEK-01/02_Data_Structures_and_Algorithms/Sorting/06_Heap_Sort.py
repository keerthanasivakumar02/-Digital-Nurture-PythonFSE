# Heap Sort Example

import heapq

numbers = [18, 7, 25, 3, 12]

heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print("Sorted Array:", sorted_numbers)