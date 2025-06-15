"""
NVIDIA, medium

You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon. 
You can assume these points are given in order; that is, you can construct the polygon 
by connecting point 1 to point 2, point 2 to point 3, and so on, finally looping around to 
connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, 
you should return False).

"""
#assign a direction to each point, make sure the point lies on the direction? wouldnt work for a weird shape

#ray casting? how to check if a point is on a line y= mx + b, and solve for that
#check if line intersects? generalzie equations, solve the system