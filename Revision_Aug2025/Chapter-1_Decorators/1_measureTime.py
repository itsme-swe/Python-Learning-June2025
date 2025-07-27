# Time Execution Function

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} ran in {end-start} time")

        return result

    return wrapper


"""
🔶 Python mein agar kisi function ke upar decorator apply kiya gaya hai, toh jab bhi wo function call hota hai, actual call decorator ke through hi hota hai.
"""


@timer
def example_function(n):
    time.sleep(n)


example_function(2)

# Output: example_function ran in 2.0004067420959473 time

# And in this above example the timer() function is actual decorator