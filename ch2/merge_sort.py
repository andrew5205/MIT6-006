
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
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1 
            k += 1



arr = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
merge_sort_recursive(arr)
print(arr)
