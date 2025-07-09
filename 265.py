"""
This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

"""

#two pass:


def calculate_bonuses(codes):
    n = len(codes)
    bonuses = [1] * n

    # Left to right
    for i in range(1, n):
        if codes[i] > codes[i - 1]:
            bonuses[i] = bonuses[i - 1] + 1

    # Right to left
    for i in range(n - 2, -1, -1):
        if codes[i] > codes[i + 1]:
            bonuses[i] = max(bonuses[i], bonuses[i + 1] + 1)

    return bonuses

# Example usage
codes = [10, 40, 200, 1000, 60, 30]
print(calculate_bonuses(codes))  # Output: [1, 2, 3, 4, 2, 1]
