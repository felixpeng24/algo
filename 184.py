"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

"""

#brute force, start from minimum number and work way down

def gcd_two(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd_two(result, num)
    return result

# Example usage
nums = [42, 56, 14]
print(find_gcd(nums))  # Output: 14


# kinda hard to visualize gcd, since a, b = b, a % b is quite random of an algorithm , other than memorization