# 🛑 STOP 
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# 🧠 UNDERSTAND
    # List of integers. Looks to be all positive from Readme and Tests. 
    # length of 1000 for tests, so data size is not tiny
    # duplicated will not always be next to eachother, as test has the numbers shuffled, and second example shows them not together.
    # there is one single number that isnot duplicated

# 🧩 PLAN
    # INPUT: arr -> an array of integers
    # OUTPUT: num -> a single integer

    # Import merge_sort from sorting
    # use merge sort to sort the array
    # for index, item in enumerate(arr)
        # if index % 2
            # if index is not equal to index + 1
                # return item

"""
from sorting import merge_sort

def single_number(arr):
# 💫 EXECUTE
    sorted = merge_sort(arr)
    count = 0
    a, b = 0, 1

    if len(sorted) % 2 == 0:
        while count < len(sorted):
            if sorted[a] == sorted[b]:
                print(a, b)
                print(sorted[a], sorted[b])
                print("---")
                a += 2
                b += 2
                count += 1

            elif sorted[a] != sorted[b]:
                return sorted[a]

    else:
        while count < len(sorted)-1:
            if a < len(sorted)-1 and b < len(sorted)-1:
                if sorted[a] == sorted[b]:
                    a += 2
                    b += 2
                    count += 1

                elif sorted[a] != sorted[b]:
                    return sorted[a]
    
            return sorted[len(sorted)-1]
"""

 # 🧩 PLAN 2.0
    # same INPUT and OUTPUT
    # maybe no need to import
    # use count() during for loop to determine if there is more than one of a given number

    # for item in arr
        # if arr.count(item) == 1:
            # return item

def single_number(arr):
# 💫 EXECUTE 2.0
    for item in arr:
        if arr.count(item) == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# 🤯 REFLECT

"""
- I forgot to think about what happens if the list is not an even number of items
- PLANNING IS IMPORTANT
"""

# 🤯 REFLECT 2.0

"""
- It is much easier to code without a migraine 🤣
"""