"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    low_index = 0
    high_index = len(input_array)-1
    #you need to have an equals sign because otherwise you will miss the part 
    #where you shring the interval to just 1 element in length. 
    while low_index <= high_index:
        #use floor division to get an integer
        midpoint = (low_index + high_index)//2
        if input_array[midpoint] == value:
            return midpoint
        elif input_array[midpoint] < value:
            #its really important to add here because otherwise if you just set
            # the value to midpoint you will get to a stage where you have an infinite
            # loop because you can't break the while loop by moving the low_index past
            # past the high_index 
            #the same is true for the high index, except what happens if you don't subtract
            # is that you get to the point where you can make the high_index less than the low
            # index and thereby break the loop. 
            low_index = midpoint +1
        elif input_array[midpoint] > value: 
            high_index = midpoint -1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
#print (binary_search(test_list, test_val1))
#print (binary_search(test_list, test_val2))
print(binary_search(test_list, test_val2))