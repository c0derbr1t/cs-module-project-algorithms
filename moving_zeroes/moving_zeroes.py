# 🛑 STOP
'''
Input: a List of integers
Returns: a List of integers
'''
# 🧠 UNDERSTAND
    # List of integers, including positive, negative, and zero
    # Length stays the same
    # List may be a mix of numbers and zeros, all numbers and no zeros, or all zeros
    # All zeroes move to the end of the list
    # all other numbers stay the same
    # returns the number of non-zero integers in the list

    # INPUT: arr -> an array of integers
    # OUTPUT: num -> a single number

# 🧩 PLAN

    # initialize a counter for number of non-zero numbers to zero
    
    # for i, item in enumerate arr
        # if item is equal to zero
            # set arr.pop(i) to a variable
            # append the popped value to the end of arr
        # elif item is not equal to zero
            # counter variable increases by one
    # return counter variable

'''
def append(arr, num):
    arr.append(num)

def moving_zeroes(arr):
    counter = 0

    for item in reversed(arr):
        if item != 0:
            counter += 1

        elif item == 0:
            popped = arr.pop(item)
            arr.append(popped)

    return arr
'''

# 🧩 PLAN 2.0
    # First did not work, so using list comprehension and then extending the first list.

def moving_zeroes(arr):
# 💫 EXECUTE 2.0

    removed = [item for item in arr if item != 0]
    zeroes = [item for item in arr if item == 0]
    removed.extend(zeroes)

    return removed


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# 🤯 REFLECT

"""
First plan did not work, but that happens a lot, and it's okay. The second plan worked well!
"""