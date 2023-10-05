#1
def minimum_value_between_values(input_dict):
    #if the dictionary is empty
    if not input_dict:
        return None

    # min_value with the first key-value pair
    min_value = next(iter(input_dict.values()))

    # Iterate through the dictionary to find the minimum value
    for value in input_dict.values():
        # value is smaller than the current min_value, update min_value
        if value < min_value:
            min_value = value

    return min_value


input_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 7, 'e': 2}
minimum_value = minimum_value_between_values(input_dict)
print("Minimum value:", minimum_value)


#2
# def factorial(n):
#     # Base case: 0! and 1! are both 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Enter a non-negative integer (n): "))

# #if n is non-negative
# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(n)
#     print(f"{n}! = {result}")
