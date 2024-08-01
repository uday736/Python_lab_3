def insertion_sort(elements):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and key < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key

# Example usage
elements = [22, 13, 4, 8, 17, 26, 53, 4]
insertion_sort(elements)
print(f"Sorted elements: {elements}")
