
# Time complexity: O(n^2)

# # pesudo
# 1. for range to all elements (i)
# 2. set reference index tracking for min val
# 3. set index j for previous element
# 4. for loop to check two value & swap 
# 5. iterate to all previous element
# 6. set min value's index to nums[i]


# # pesudo - P18

# for i = 2 to Arr.len
#     key = Arr[i]
#     # insert Arr[i] to sorted sequence 
#     j = i - 1
#     while j > 0 and Arr[j] > key 
#         Arr[j+1] = Arr[j]
#         j -= 1
#     Arr[j+1] = key



def insertion_sort(nums):
    
    # starting at second element as assume the first is sorted
    for i in range(1, len(nums)):
        
        # keep a reference while running compairing
        key = nums[i]
        
        # index to compare with the previous element
        j = i - 1   
        
        while j >= 0 and nums[j] > key:
            # if the sorted side element is greater, have to copy to the next/ right side position(moving)
            nums[j+1] = nums[j]
            
            # compare backwards
            j -= 1
        
        # Insert item
        nums[j+1] = key


my_list = [9, 1, 15, 28, 6]
insertion_sort(my_list)
print(my_list)

