# ex1
from functools import reduce

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example usage
my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print("Result:", result)



# ex2
def count_upper_lower_case(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return upper_count, lower_count

# Example usage
text = "Hello World"
upper, lower = count_upper_lower_case(text)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)



# ex3
def is_palindrome(text):
    return text == text[::-1]

# Example usage
text = "radar"
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




# ex4
import time
import math

def square_root_with_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

# Example usage
number = 25100
delay = 2123
result = square_root_with_delay(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")



# ex5
def all_true(elements):
    return all(elements)

# Example usage
my_tuple = (True, True, True, True)
print(all_true(my_tuple))  # Output: True
