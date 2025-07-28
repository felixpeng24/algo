"""Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2

"""

def has_pythagorean_triplet(arr):
    arr.sort()
    n = len(arr)

    # Square all elements in-place
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    # Fix one element (c^2) and find a^2 + b^2 = c^2
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if arr[left] + arr[right] == arr[i]:
                return True
            elif arr[left] + arr[right] < arr[i]:
                left += 1
            else:
                right -= 1
    return False
