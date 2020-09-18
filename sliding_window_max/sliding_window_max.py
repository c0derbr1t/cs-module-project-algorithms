# 🛑 STOP
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# 🧠 UNDERSTAND
    # given an array of numbers, positive and negative
    # given a window size that will slide along the list
    # need to find the largest number in the window as it moves along the list one by one
    # create a new List of the greatest numbers
    # return that created list
    # tests include normal and a file with 1 MILLION numbers in the array, and a window size of 1000!!!!

    # INPUTS: arr -> an array of integers (tests for normal, and large inputs)
    # OUTPUT: arr -> an array of the largest numbers

# 🧩 PLAN
    # max_nums variable for empty array
    # sub_arr variable for window set to empty array
    # a, b set to k-k and k-1
    # while len(max_nums) != len(arr)-2
        # sub_arr = a slice of arr[a:b]  -> slice the list to get the "window"
        # max_val = max(sub_arr)
        # max_nums.append(max_val)
        # a + 1
        # b + 1

# O(n*k) time, O(n)
def sliding_window_max(nums, k):
# 💫 EXECUTE
    max_nums = []
    sub_nums = []
    a, b = k-k, k

    while b != len(nums)+1:
        sub_nums = nums[a:b]
        max_val = max(sub_nums)
        max_nums.append(max_val)
        a += 1
        b += 1

    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


# 🤯 REFLECT
# I took more time with planning and thinking this one out, and it worked well! This one was still difficult for the small amount of lines.