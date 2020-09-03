def linear_search(arr, target):
    # loop through each item in the array
    for item in arr:
        # check if the item in the array is equal to the target
        if item == target:
            # if the item is equal to the target return the index of the item
            return arr.index(item)
    return -1 # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    return -1  # not found
