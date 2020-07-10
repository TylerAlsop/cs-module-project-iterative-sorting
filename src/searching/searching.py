def linear_search(arr, target):
    # Your code here

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        middle_index =  (first_index + last_index) // 2
        middle_item =  arr[middle_index]

        if target == middle_item:
            return middle_index
        elif target < middle_item:
            last_index =  middle_index -1
        else:
            first_index = middle_index + 1

    return -1  # not found
