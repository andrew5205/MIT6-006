
from heapq import heappop, heappush

# heappush(list, item) - adds an element to the heap, and re-sort it afterward so that it remain a heap. 
# heappop(list, item) - pop a first(smallest) element and RETURN that element. the heap remain the heap. so no need max_heapify()
# heapify(list) - turn the given list into a heap. 


def heap_sort(arr):
    heap = []
    for e in arr:
        heappush(heap, e)
    
    ordered = []

    while heap:
        ordered.append(heappop(heap))
    
    return ordered 

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))         # [2, 4, 5, 13, 15, 17, 18, 21, 24, 26]
# ******************************************************************************************************************

# O(n logn)
# heapify - a process of converting a binary tree into a heap data
# heapify - All it does is looking into parent and two children, swap if needed 

# A heap must be a complete binary tree, that's each level of tree is completelly filled, except possibly the bottom level 
# it is filled from LEFT to RIGHT


def max_heapify(arr, heap_size, root_index):
    
    # define 3 index: root(Top parent), left, right 
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    # if the left_child of the root is vaild, and the element is greater than current root(largest), update the largest element 
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child
    else:
        largest = root_index
    # if the right_child of the root is vaild, and the element is greater than current root(largest), update the largest element
    if right_child < heap_size and arr[right_child] > arr[right_child]:
        largest = right_child

    # If the the largest element is no longer root element, swap 
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        # recursive
        max_heapify(arr, heap_size, largest)



