# Time Complexity Example
# This program prints the square of each number.

def print_squares(n):
    for i in range(1, n + 1):
        print(f"Square of {i} = {i * i}")


print("Time Complexity: O(n)")
print_squares(5)