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
    # check if the length of the array has at least one item
    if 0 < len(arr):
        # set the starting pointer value to 0
        start_pointer = 0
        # set the end_pointer to the length of the array minus one to get the last index value
        end_pointer = len(arr) - 1
        # while the starting pointer value is less than the end pointer value
        while start_pointer <= end_pointer:
            # find the midpoint index betweent he start and end pointer
            midpoint_pointer = (start_pointer + end_pointer) // 2
            # check if the target is less than the index of the value of the midpoint index 
            if target < arr[midpoint_pointer]:
                # reset the end_pointer to the midpoint
                end_pointer = midpoint_pointer
            # else check if the target is greater than the index of the value of the midpoint index
            elif target > arr[midpoint_pointer]:
                # if it is set the starting point to the midpoint
                start_pointer = midpoint_pointer
            else:
                # else the target is equal to the midpoint
                return midpoint_pointer
    return -1  # not found
