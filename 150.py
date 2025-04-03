"""
Given a list of points, a central point, and an integer k, find the nearest k points 
from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point 
(1, 2), and k = 2, return [(0, 0), (3, 1)].


"""

#doesnt seem too tough, although its supposed to be hard
#distance formula calculation, find the lowest two numbers and output those points?r
# yes but use min heap

import heapq

def k_nearest_points(points, center, k):
    # Compute distances and use a min-heap to get the k smallest
    heap = []
    
    for point in points:
        x, y = point
        cx, cy = center
        distance = (x - cx) ** 2 + (y - cy) ** 2  # Squared Euclidean distance
        heapq.heappush(heap, (distance, point))  # Store as (distance, point)

    # Extract k smallest points
    return [heapq.heappop(heap)[1] for _ in range(k)]

# Example usage:
points = [(0, 0), (5, 4), (3, 1)]
center = (1, 2)
k = 2

print(k_nearest_points(points, center, k))
