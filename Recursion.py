# Recursion to sum numbers
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])  # [1:] includes all elements of the list except the first

# Recursion to count the number of items in a list
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

# Recursion to find the maximum number in a list
def max(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    temp_max = max(list[1:])
    if list[0] > temp_max:
        return list[0]
    else:
        return temp_max    
    
list = [1, 2, 3, 5, 7, 9]
result = max(list)
print(result)
    