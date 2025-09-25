""""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].

"""

#divide and conquer, when merging, split inoto rectangle and compare there

from math import hypot

def closest_pair(points):
    if len(points) < 2:
        return None, float("inf")

    Px = sorted(points)                     # sort by x, then y
    Py = sorted(points, key=lambda p: p[1]) # sort by y

    def dist2(a, b):
        dx, dy = a[0]-b[0], a[1]-b[1]
        return dx*dx + dy*dy

    def brute(pts):
        best = (None, None, float("inf"))
        n = len(pts)
        for i in range(n):
            for j in range(i+1, n):
                d2 = dist2(pts[i], pts[j])
                if d2 < best[2]:
                    best = (pts[i], pts[j], d2)
        return best

    def rec(Px, Py):
        n = len(Px)
        if n <= 3:
            return brute(Px)

        mid = n // 2
        midx = Px[mid][0]
        Lx, Rx = Px[:mid], Px[mid:]

        Ly, Ry = [], []
        for p in Py:                         # linear split by x-side while preserving y-order
            (Ly if p[0] <  midx or (p[0] == midx and p in Lx) else Ry).append(p)

        (p1L, p2L, d2L) = rec(Lx, Ly)
        (p1R, p2R, d2R) = rec(Rx, Ry)
        if d2L <= d2R:
            best_pair, best_d2 = (p1L, p2L), d2L
        else:
            best_pair, best_d2 = (p1R, p2R), d2R

        # Build strip: points within sqrt(best_d2) of midline
        strip = [p for p in Py if (p[0] - midx)**2 < best_d2]

        # Check each strip point against next up to 7 by y
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1])**2 < best_d2:
                d2 = dist2(strip[i], strip[j])
                if d2 < best_d2:
                    best_d2 = d2
                    best_pair = (strip[i], strip[j])
                j += 1

        return best_pair[0], best_pair[1], best_d2

    a, b, d2 = rec(Px, Py)
    return (a, b), hypot(a[0]-b[0], a[1]-b[1])

# Example
pts = [(1,1), (-1,-1), (3,4), (6,1), (-1,-6), (-4,-3)]
pair, dist = closest_pair(pts)
print(pair, dist)  # → ((-1, -1), (1, 1)) 2.8284271247461903
