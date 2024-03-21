def is_palindrome(word):
    cleaned_word = "".join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]

user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
