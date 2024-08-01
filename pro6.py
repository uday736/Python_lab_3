def selection_sort(elements):
    for i in range(len(elements)):
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        elements[i], elements[min_index] = elements[min_index], elements[i]

# Example usage
elements = [22, 13, 4, 8, 17, 26, 53, 4]
selection_sort(elements)
print(f"Sorted elements: {elements}")
