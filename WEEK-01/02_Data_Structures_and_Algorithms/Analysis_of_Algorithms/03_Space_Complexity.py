# Space Complexity Example
# This program stores the cubes of numbers in a list.

def create_cube_list(n):
    cubes = []

    for i in range(1, n + 1):
        cubes.append(i ** 3)

    return cubes


result = create_cube_list(5)

print("Space Complexity: O(n)")
print(result)