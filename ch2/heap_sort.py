
from heapq import heappop, heappush

# heappush(list, item) - adds an element to the heap, and re-sort it afterward so that it remain a heap. 
# heappop(list, item) - pop a first(smallest) element and RETURN that element. the heap remain the heap. so no need heapify()
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





