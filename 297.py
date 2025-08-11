"""
This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

"""

#dp?
#or heuristic it by summing up frequency? greedy
#greedy it is

def greedy_min_drinks(preferences):
    uncovered = set(preferences.keys())
    drink_map = {}
    for c, ds in preferences.items():
        for d in ds:
            drink_map.setdefault(d, set()).add(c)

    chosen = []
    while uncovered:
        # pick drink that covers the most uncovered customers
        d, covered = max(
            ((d, cov & uncovered) for d, cov in drink_map.items()),
            key=lambda x: len(x[1])
        )
        if not covered:
            return None  # impossible to satisfy all customers
        chosen.append(d)
        uncovered -= covered
    return chosen
