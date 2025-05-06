"""
Let X be a set of n intervals on the real line. We say that a set of points 
P "stabs" X if every interval in X contains at least one point in P. Compute 
the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].

"""

def stab_intervals(intervals):
    # Sort intervals by their end points
    intervals.sort(key=lambda x: x[1])
    stabbing_points = []
    last_point = None

    for interval in intervals:
        if last_point is None or not (interval[0] <= last_point <= interval[1]):
            # Add the end of the current interval
            last_point = interval[1]
            stabbing_points.append(last_point)
    
    return stabbing_points

# Example
print(stab_intervals([(1, 4), (4, 5), (7, 9), (9, 12)]))  # Output: [4, 9]
