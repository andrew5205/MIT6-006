
# selection sort - compare each elements, 
#                   continuously remove the smallest element of unsorted segment(RIGHT) of the list to the sorted segment (LEFT)
# find the lowest val, get it's index, and then swap with index i at the end of single loop j


# sorted + unsorted
# as i increased, we check less items
# 
# Time complexity: O(n^2)

# # pesudo
# 1. nested for loop 
# 2. low_val_index = i, 
# 3. j start as i + 1, compare min val and store IndexError
# 4. swap 



def selection_sort(nums):
    
    for i in range(len(nums)):
        
        lowest_val_index = i
        
        # start point is the next element of i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_val_index]:
                lowest_val_index = j
        # after the lowest val was found, get it's index and swap 
        nums[i],  nums[lowest_val_index] = nums[lowest_val_index], nums[i]



my_list = [12, 5, 8, 3, 25, 16]
selection_sort(my_list)
print(my_list)




