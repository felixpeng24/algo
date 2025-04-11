"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""

#go through each one, assign a letter using hash, see if any left over?

def has_one_to_one_mapping(s1, s2):
    if len(s1) != len(s2):
        return False

    mapping = {}
    mapped_values = set()

    for c1, c2 in zip(s1, s2):
        if c1 in mapping:
            if mapping[c1] != c2:
                return False  # Inconsistent mapping
        else:
            if c2 in mapped_values:
                return False  # Another character already maps to c2
            mapping[c1] = c2
            mapped_values.add(c2)

    return True
