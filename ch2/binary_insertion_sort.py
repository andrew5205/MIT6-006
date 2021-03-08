
# O( n log n)

# binarty search takes O(log n) time
# shifting elements takes O(n) time

def InsertionSort_improved(A):
    for k in range(1,len(A)):
        key = A[k]
        low = 0
        high = k-1
        BinarySearch(A, low, high, key, k)

def BinarySearch(A, low, high, key, k):
    if low < high:
        mid = (low + high) // 2
        if A[mid] == key:
            for i in range(k, mid, -1):
                A[i] = A[i-1]
            A[i-1] = key
        elif A[mid] < key:
            BinarySearch(A, mid+1, high, key, k)
        else:
            BinarySearch(A, low, mid, key, k)
    else:
        mid=(low + high) // 2
        if A[mid] > key:
            for j in range(k, mid, -1):
                A[j] = A[j-1]
            A[j-1] = key
            
my_list = [3, 25, 18, 41, 52, 26, 38, 57, 9, 49]
InsertionSort_improved(my_list)
print(my_list)