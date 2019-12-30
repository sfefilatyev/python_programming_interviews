# Implemented naively, quicksort has large run times and deep function call stack on arrays with
# many duplicates because the subarrays may differ greatly in size. One solution is to re-order 
# the array so that all eleemnts less than pivot appear first, followed by elements equal to the 
# pivot, followed by elements greater than the pivot. This is known as Dutch national flag 
# partitioning, because the Dutch national flag consists of three horizontal bands, each in a 
# different color. 
#
# Write a program that takes an array A an dan index i into A, and re-arranges 
# the elements such that all elements less than A[i] appear first, followed by elements equal to 
#the pivot, followed by elements greater than the pivot.

A = [1, 6, 3, 4, 5, 2, 7]
print("Before sorting:")
print(A)
index = 3

def dutch_flag_partitioning(A, i):
    """Partition input array A according to Dutch partitioning using input index i."""
    pivot = A[i]
    # `lower` is the index of the last element of array from the left that is lower than pivot.
    lower = 0
    # `equal` is  the index of the first unclassified element from the left.
    equal = 0
    # `larger` is the index of the border element from the right of the array that is larger
    # than pivot.
    larger = len(A) 
    while equal < larger:
        if A[equal] < pivot:
            A[lower], A[equal] = A[equal], A[lower]
            lower += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
    return A


print("After partitioning on i={}".format(index))
print(dutch_flag_partitioning(A, index)) 

