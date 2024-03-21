def print_permutations(input_string):
    from itertools import permutations
    perm_list = list(permutations(input_string))
    for perm in perm_list:
        print("".join(perm))

user_input = input("Enter a string: ")
print_permutations(user_input)
