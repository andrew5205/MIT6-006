
# O(n log n) - Time complexity 
# O(n) - auxiliary space

# divide & conquer

def merge_sort_recursive(arr):
    
    # base case, divide untill single element 
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
        # recursion
        merge_sort_recursive(left_arr)
        merge_sort_recursive(right_arr)

        # merge
        i = 0   # left arr index 
        j = 0   # right arr index
        k = 0   # merged arr index 

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        # make sure left & right all parse to the end

        # case: right_arr empty first 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # case: left_arr empty first
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1 
            k += 1



arr = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
merge_sort_recursive(arr)
print(arr)








# ********************************************************************************************
def merge(left, right):
    left_index, right_index = 0, 0
    result= []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(arr):
    # base case 
    if len(arr) <= 1:
        return arr
    
    half = len(arr) // 2 
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)


array = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(merge_sort(array))


