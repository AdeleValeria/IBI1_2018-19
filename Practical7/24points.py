# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:42:24 2019

@author: Adele
"""

import operator
from itertools import permutations

input_numbers = input("Type some numbers between 1 and 23: ").split(",")
#The map() function executes a specified function for each item in a iterable.
#In this case, the numbers in the list are converted to integer
input_numbers = list(map(int, input_numbers))
target = 24
#Can only contain numbers between 1 and 23
#The length of the input does not matter
valid_number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,23)
check = all(i in valid_number for i in input_numbers)
     

math_operation = {"add": operator.add, "mul": operator.mul, "sub": operator.sub, "div": operator.truediv}

symbols = {"add": "+", "mul": "*", "sub": "-", "div": "/"}

count = 0
def grouping(nums):
    #Count the recursion times
    global count
    count = count + 1
    if len(nums) == 1:
        yield nums[0]
    elif len(nums) == 2:
        yield nums
    else:
        yield from (
            (x, y)
            for i in range(1, len(nums))
            for x in grouping(nums[:i])
            for y in grouping(nums[i:])
        )


def get_groupings(nums2):
    global count
    count = count + 1
    for nums in nums2:
        yield from grouping(nums)


def _generate_candidates(nums):
    global count
    count = count + 1
    x, y = nums[0], nums[1]
    if not isinstance(x, tuple) and not isinstance(y, tuple):
        for name in math_operation:
            yield (name, x, y)
    else:
        x_gens = [x] if not isinstance(x, tuple) else _generate_candidates(x)
        y_gens = [y] if not isinstance(y, tuple) else _generate_candidates(y)
        yield from (
            (name, a, b) for a in x_gens for b in y_gens for name in math_operation
        )


def generate_candidates(numbers):
    global count
    count = count + 1
    all_permutations = (
        x for r in range(2, len(numbers) + 1) for x in permutations(numbers, r)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def compute(candidate):
    global count
    count = count + 1
    name, x, y = candidate
    child_x, child_y = x, y
    child_x = compute(x)[1] if isinstance(x, tuple) else x
    child_y = compute(y)[1] if isinstance(y, tuple) else y
    return candidate, math_operation[name](child_x, child_y)


def get_best_candidates(candidates, final_result):
    global count
    count = count + 1
    best_candidate, best_result, exact_found = None, 0, False
    for candidate in candidates:
        try:
            n, r = compute(candidate)
        except (ValueError, ZeroDivisionError, TypeError, OverflowError):
            continue
        if abs(r - final_result) < abs(best_result - final_result):
            best_candidate, best_result = n, r
        if r == final_result:
            exact_found = True
            yield r, n
    if not exact_found:
        yield best_result, best_candidate


def parse(candidate, bracket=True):
    global count
    count = count + 1
    name, x, y = candidate
    symbol = symbols[name]
    child_x = parse(x) if isinstance(x, tuple) else str(x)
    child_y = parse(y) if isinstance(y, tuple) else str(y)
    result = f" {symbol} ".join([child_x, child_y])
    if bracket:
        return f"({result})"
    return result


solution = 0

if check is True and len(input_numbers) != 1: 
    for (x, y) in get_best_candidates(generate_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        #Count how many ways to reach the target number
        solution = solution + 1 
    #If there are not enough numbers to reach the target
    if solution < 2:
        solution = 0
        print("No solution found\nThere are not enough numbers to get", target)
    else:
        print("There are", solution, "ways to get", target)
#In case the user only gives 1 number
elif len(input_numbers) == 1:
    print("No solution found. Please input more than 1 number.")
#If the number given is above 23 or below 1
elif check is False:
    print("The numbers must be between 1 and 23")  

print('Recursion times:', count)