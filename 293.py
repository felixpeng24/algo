"""
You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone,
 after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary. Given this information, determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].

"""

def min_cost_to_pyramid(stones):
    n = len(stones)
    min_cost = float('inf')

    for center in range(n):
        max_height = 1

        # Determine the max possible height at this center
        while True:
            left = center - (max_height - 1)
            right = center + (max_height - 1)

            if left < 0 or right >= n:
                break  # pyramid won't fit

            valid = True
            cost = 0
            for i in range(left, right + 1):
                required_height = max_height - abs(i - center)
                if stones[i] < required_height:
                    valid = False
                    break
                cost += stones[i] - required_height

            if valid:
                min_cost = min(min_cost, cost)
                max_height += 1
            else:
                break

    return min_cost
