def quicksort(arr):
    # Base case: If the input array has 0 or 1 elements, it's already sorted
    if len(arr) < 2:
        return arr

    else:
        # Select the first element as the pivot
        pivot = arr[0]

        # Initialize empty lists to store elements less than and greater than the pivot
        less = []
        greater = []

        # Iterate through elements in the array starting from the second element (index 1)
        for i in arr[1:]:
            # If the current element is less than or equal to the pivot, append it to the 'less' list
            if i <= pivot:
                less.append(i)
            # If the current element is greater than the pivot, append it to the 'greater' list
            else:
                greater.append(i)

        # Recursively sort the 'less' and 'greater' lists and combine them with the pivot to form the sorted array
        return quicksort(less) + [pivot] + quicksort(greater)

# Example array
arr = [10, 5, 2, 3]
print(quicksort(arr))
