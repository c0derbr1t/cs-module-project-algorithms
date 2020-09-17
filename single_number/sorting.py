# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    size_A = len(arrA)
    size_B = len(arrB)
    merged_arr = []

    a, b = 0, 0

    while a < size_A and b < size_B:
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1

        else:
            merged_arr.append(arrB[b])
            b += 1

    merged_arr = merged_arr + arrA[a:] + arrB[b:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    else:

        middle = len(arr) // 2
        left = arr[0:middle]
        right = arr[middle:len(arr)]
        new1 = merge_sort(left)
        new2 = merge_sort(right)
        new_arr = merge(new1, new2)


        return new_arr

# one = [1, 2, 3, 4, 5]
# two = [5, 7, 8, 9, 10, 11, 12, 13]
# print(merge(one, two))

# unsorted = [ 5, 29, 38, 3, 6, 18, 4, 39, 1, 50, 0, 12, 9, 8, 7, 2]
# print(merge_sort(unsorted))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

