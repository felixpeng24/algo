"""
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 
678 is not a palindrome. Do not convert the integer into a string.

"""

def is_palindrome(num):
    if num < 0:
        return False  # negative numbers are not palindromes

    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original == reversed_num

# Example usage
print(is_palindrome(121))  # True
print(is_palindrome(888))  # True
print(is_palindrome(678))  # False
print(is_palindrome(-121)) # False


#yes so u do use modulus