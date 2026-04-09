#Write a program to make use of map(), filter() and reduce() functions 
#with context to lambda functions.
from functools import reduce

nums = [10, 15, 20, 25, 30]

half_values = list(map(lambda x: x / 2, nums))

greater_than_20 = list(filter(lambda x: x > 20, nums))

product = reduce(lambda x, y: x * y, nums)

print("Original List:", nums)
print("Half Values (map):", half_values)
print("Numbers > 20 (filter):", greater_than_20)
print("Product (reduce):", product)
