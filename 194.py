"""

Suppose you are given two lists of n points, one list p1, p2, ..., pn on the 
line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n 
line segments connecting each point pi to qi. Write an algorithm to determine how many 
pairs of the line segments intersect.


Easy

"""

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions

def count_segment_intersections(p_list, q_list):
    # Assume both p_list and q_list are lists of x-coordinates
    pairs = list(zip(p_list, q_list))
    pairs.sort(key=lambda x: x[0])  # Sort by p_i (x-coordinates on y = 0)
    q_sequence = [q for _, q in pairs]
    return count_inversions(q_sequence)

#thats not fair
