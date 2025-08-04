"""
An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, 
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

"""

#two pointer greedy sort, ezpz


def num_rescue_boats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # Check if the lightest and heaviest person can share a boat
        if people[left] + people[right] <= limit:
            left += 1  # pair is possible, move left pointer

        # In both cases, the heavier person goes, so move right pointer
        right -= 1
        boats += 1

    return boats



#time: nlogn
#space: o1