# 🛑 STOP
'''
Input: a List of integers
Returns: a List of integers
'''
# 🧠 UNDERSTAND
    # All numbers are positive. Look to be numbers 1-10.
        # Other cases may happen, but none are shown, when using division.
        # If NOT utilizing division, 0 may be present!
    # multiply all numbers except itself in that spot.

    # INPUT: arr -> a list of positive integers
    # OUTPUT: arr -> a list of multiplied integers


# 🧩 PLAN
    # import math
    # intitialize product variable to 0
    # for i, item in enumerate(arr)
        # arr.remove(item)  -> remove the item out of the list so it is not calculated.
        # product = math.prod(arr) -> get the product of all of the other values
        # arr.insert(i, product) -> insert the product in the removed item's spot.

    # Possible problems:
        # inserting in the wrong place!
        # Killed VS Code 🤣

'''
import functools

def multiply(a, b):
    return a * b

def product_of_all_other_numbers(arr):
# 💫 EXECUTE
    for i, item in enumerate(arr):
        print(arr)
        arr.remove(item)
        print(arr)
        product = functools.reduce(multiply, arr)
        print(product)
        arr.insert(i, product)
        print(arr)

    return arr
'''

# 🧩 PLAN 2.0
    # import math module
    # set a variable for an empty array
    # for index and item in enumerated array
        # pop out the current item and set it to a variable
        # set math.prod(arr) to a variable (works with python v. 3.8)
        # insert the popped value out back into it's place
        # append the product to the array we are building

    # return the array that is built

import math

def product_of_all_other_numbers(arr):
# 💫 EXECUTE 2.0
    multiplied = []

    for i, item in enumerate(arr):
        popped = arr.pop(i)
        product = math.prod(arr)
        arr.insert(i, popped)
        multiplied.append(product)

    return multiplied

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# 🤯 REFLECT
# Tried too hard to do it well the first time. Trying a second time to just get it to work!

# 🤯 REFLECT 2.0
# prod() is an amazing thing to have. This seems a little more complicated without it. Nothing else I was trying worked!
# for loop has i, item and is enumerated, but item is not used. Look for a way to do it without enumerating?