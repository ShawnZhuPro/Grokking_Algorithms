# O(log n) AKA log time
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        
        if guess == item:  # If the guessed value is equal to the item we're searching for
            return mid  # Returns the index where the item is found
        
        if guess > item:  # If the guessed value is greater than the item
            high = mid - 1  # Adjusts the upper bound to search in the lower half
        else:
            low = mid + 1  # Adjusts the lower bound to search in the upper half
        
    return None  # Returns None if the item is not found in the list

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # Output should be the index of 1
print(binary_search(my_list, 0)) # Output should be None