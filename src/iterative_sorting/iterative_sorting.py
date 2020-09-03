# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                # TO-DO: swap
                # Your code here
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sorted = False
    while not sorted:
        sorted = True
        # loop through the array
        for item in range(0, len(arr) - 1):
            # compare each element to its neighbor
            # if elements in wrong position (relative to each other, swap them)
            if arr[item] > arr[item + 1]:
                sorted = False
                arr[item], arr[item + 1] = arr[item + 1], arr[item]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    # initialize the max_value and set to None
    max_value = None
    
    # check if the maximum value is passed in and is not None
    if maximum is not None:
        # if it is passed in set the max value to the maximum + 1
        max_value = maximum + 1
    # if maximum is None check if their are items in the array
    elif 0 < len(arr):
        # if there are set the max_value to the max of the passed in array + 1
        max_value = max(arr) + 1
    
    # if the max value is passsed and and the value is greater than 0
    if (max_value is not None) and (0 < max_value):
        # create the counting list buckets by creating array buckets of 0 times the max_value
        counting_list = [0] * max_value
        # loop through each item in the array
        for item in arr:
            # if 0 is less than or equal to the itme
            if 0 <= item:
                # increase the bucket of the counting list by 1
                counting_list[item] += 1
            # otherwise a negative number was passed in and we should send the error
            else:
                return "Error, negative numbers not allowed in Count Sort"
        # initialize pointer index
        pointer_index = 0
        # for each item in the ranger of the length of the number of buckets in the counting_list
        for i in range(len(counting_list)):
            # loop while the index of the counting list of i is greater than 0
            while 0 < counting_list[i]:
                # set the value of the arr at the pointer to i
                arr[pointer_index] = i
                # decrease the value of the counting_list bucket we are at by 1
                counting_list[i] -= 1
                # increase the pointer_index by 1
                pointer_index += 1
    # return the passed in arr
    return arr
