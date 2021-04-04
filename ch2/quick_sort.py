

# partition
# average: O(log n)
# worst: O(n^2)


def quick_sort(arr):
    
    length = len(arr)
    
    # base case
    if length <= 1:
        return arr
    else:
        # always take the last element from arr as pivot
        pivot = arr.pop()

    greater = []
    lower = []

    # partition -> lower + pivot + greater
    for e in arr:
        if e > pivot:
            greater.append(e)
        else:
            lower.append(e)
            
    # recursion
    return quick_sort(lower) + [pivot] + quick_sort(greater)




arr = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 0]
print(quick_sort(arr))

