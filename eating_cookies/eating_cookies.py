# 🛑 STOP
'''
Input: an integer
Returns: an integer
'''
# 🧠 UNDERSTAND
    # given one number as the number of 🍪 in the cookie jar that Cookie Monster gets to eat!
    # need to find all of the ways he can eat those cookies.
    # Cookie Monster can eat 1, 2, or 3 🍪 at one time.
    # Example:
        # If the jar has 3 🍪...there are 4 possible ways for Cookie Monster to eat them all:
            # He can eat 1 🍪 at a time, 3 times
            # He can eat 1 🍪 , then 2 🍪 
            # He can eat 2 🍪 , then 1 🍪 
            # He can eat all 3 🍪  at once
        # SO, eating_cookies(3) should return an answer of 4.

    # Use recursion
    
    # Can you eat 0 cookies?
        # There is 0 ways to eat 0 cookies, as you aren't eating them.

    # Can you eat a neg number of cookies?
        # You cannot un-eat cookies (unless you eat too many of them...which never happens for Cookie Monster).

    # REMEMBER: DOES NOT NEED TO BE SUPER PERFORMANT YET!!!

# 🧩 PLAN
    #X set nums variable to empty list
    #X for i in range(1, (n+1)
        #X nums.append(i)

    # EC: ec(n-1) + ec(n-2) + ec(n-3)
    # Recursive version using similar to the fibinocci sequence -> O(3^n)

# O(3^n)
def first_eating_cookies(n):
# 💫 EXECUTE
    # what are our base cases
    # this represents there being a number of cookies where we can take just that many cookies
    if n < 0:
        return 0
    if n == 0:
        return 1
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# Using caching/memoization, the runtime is now O(n)
def eating_cookies(n, cache=None):
# 💫 EXECUTE
    # what are our base cases?
    if n < 0:
        return 0
    # this represents there being a number of cookies where we can just take
    # that many cookies
    elif n == 0:
        return 1
    # check the cache to see if the answer is stored in there
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# 🤯 REFLECT
# This is a super hard problem. The first answer focuses on understanding how it works with the fibinocci sequence. It was went over in class, and I still don't understand what is happening very well.

# It makes more sense near the end of class now.