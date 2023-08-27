def findSmallest(arr):
    # Initializes the smallest element and its index to the first element
    smallest = arr[0]
    smallest_index = 0
    
    # Loops through the array starting at the 2nd element
    for i in range (1, len(arr)):
        # Compares the current element to the smallest so far
        if arr[i] < smallest:
            # Replaces the old smallest element with the new smallest element
            smallest = arr[i]
            smallest_index = i
        
    return smallest_index

def selectionSort(arr):
    # Initializes a new, empty array for sorted elements to be stored
    newArr = []

    # Loops through the original array
    for i in range (len(arr)):
        # Implements the findSmallest function then removes the smallest element
        # in the original array and appends it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([5,3,6,2,10]))  # Output should be sorted from smallest -> largest