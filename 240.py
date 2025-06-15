"""
This problem was asked by Spotify. Hard

There are N couples sitting in a row of length 2 * N. They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?


Each couple can be represented by person // 2, since (0,1) → 0, (2,3) → 1, etc.

To fix the row, we can go two-by-two and if the two people are not in the same couple, swap one with their actual partner.
"""

#first reaction dp, base case:
#n=2, 1
#3, 1+ n=2

#misunderstood problem, whoops:
# its jsut iyterative......

def min_swaps_couples(row):
    n = len(row)
    pos = {person: i for i, person in enumerate(row)}
    swaps = 0

    for i in range(0, n, 2):
        first = row[i]
        expected_partner = first ^ 1  # Partner in the same couple
        if row[i + 1] != expected_partner:
            partner_idx = pos[expected_partner]

            # Swap
            row[i + 1], row[partner_idx] = row[partner_idx], row[i + 1]

            # Update positions
            pos[row[partner_idx]] = partner_idx
            pos[row[i + 1]] = i + 1

            swaps += 1

    return swaps
