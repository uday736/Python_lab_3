def sequential_search(elements, target):
    for i, element in enumerate(elements):
        if element == target:
            return i
    return -1  # Not found

elements = [1, 3, 5, 8, 10, 23, 35]
target = 10
index = sequential_search(elements, target)
print(f"Element {target} found at index {index}")
