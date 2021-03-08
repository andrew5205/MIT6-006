# https://stackabuse.com/sorting-algorithms-in-python/

# Bubble sort - iterates over a LIST, 
#                 comparing elements is pairs and swapping them unti the larger elements "bubble up" to the end of the list 


# Time complexity: O(n^2)

# # pesudo
# 1. use while 
# 2. for loop for swap condition
# 3. define True cases: swapped


def bubble_sort(nums):
    
    swapped = True

    # break the while loop only when no more elements are swapped( done with for loop/ for ALL)
    while swapped:

        swapped = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True



my_list = [5, 1, 2, 8, 4]
bubble_sort(my_list)
print(my_list)




