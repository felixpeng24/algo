"""
You are given an array representing the heights of neighboring buildings on a city street, from east to west. The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?

"""

def rightpass(nums):
    maxH = 0
    houses = 0
    for num in nums[::-1]:
        if num > maxH:
            houses += 1
        maxH = max(maxH, num)
    return houses

print(rightpass([3, 7, 8, 3, 6, 1]))


def oneforwardpass(nums):
    #lenght - shaded buildings?