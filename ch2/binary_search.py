
# O(lg n) time 
# low, high, mid are index 


# Iterate method
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1 
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        
        if mid_val == key:
            return mid
        elif mid_val > key:
            high = mid - 1
        else:
            low = mid + 1
    return None



# Recursive method 
# similar to iterative, chage in pass in arguements

def binary_search_recursive(arr, key, low, high):
    
    # base case 
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val == key:
            return mid 
        elif mid_val > key:
            # recursive, pass mid-1 as high index 
            return binary_search_recursive(arr, key, low, mid-1)
        else:
            # recursive, pass mid+1 as low index 
            return binary_search_recursive(arr, key, mid+1, high)





data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15]
key = 12 

print(binary_search_iterative(data, key))

print(binary_search_recursive(data, key, 0, len(data)-1))






