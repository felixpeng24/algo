"""
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""

def get_bounds(rect):
    x1, y1 = rect["top_left"]
    width, height = rect["dimensions"]
    x2 = x1 + width
    y2 = y1 - height
    return x1, y1, x2, y2  # top-left to bottom-right

def rectangles_overlap(rect1, rect2):
    x1_1, y1_1, x2_1, y2_1 = get_bounds(rect1)
    x1_2, y1_2, x2_2, y2_2 = get_bounds(rect2)
    
    return not (x2_1 <= x1_2 or x1_1 >= x2_2 or y2_1 >= y1_2 or y1_1 <= y2_2)

def any_rectangles_overlap(rectangles):
    n = len(rectangles)
    for i in range(n):
        for j in range(i + 1, n):
            if rectangles_overlap(rectangles[i], rectangles[j]):
                return True
    return False

# Example usage
rectangles = [
    {"top_left": (1, 4), "dimensions": (3, 3)},
    {"top_left": (-1, 3), "dimensions": (2, 1)},
    {"top_left": (0, 5), "dimensions": (4, 3)}
]

print(any_rectangles_overlap(rectangles))  # Output: True
