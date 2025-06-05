"""

Given a string with repeated characters, 
rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.


"""

#iterate through string, have a curr var, and also a list of indices that are adjacent? then everytime you it a new char, pop from queue

#usign a max heap for frequency, python defauts to min heap


import heapq
from collections import defaultdict

def adjacentChar(s):
    heap = []
    res = []
    charHash = defaultdict(int)
    for char in s:
        charHash[char] -= 1  #negating for max heap since python deafults to min heap
    
    for key, value in charHash.items():
        heap.append((value, key))  #creting tuples inside array
    
    heapq.heapify(heap) #now we have a max heap

    #so what do we do from here with a max heap? we append it, drop freq, move it to temp var for cooldown, repeat, move back in temp var, keep going until theres nothing left
    #we would end up with, for something like aaab, abaa, so we can do a final check at the end
    prev = None
    while heap:
        if prev and heap:
            heapq.heappush(heap, prev)

        freq, char = heapq.heappop(heap)
        res.append(char)

        if freq + 1 != 0:
            prev = (freq + 1, char)
        else:
            prev = None

    #final check

    for i in range(1, len(res)):
        if res[i] == res[i-1]:
            return None

    return ''.join(res)

print(adjacentChar("aaabbc"))



import heapq
from collections import defaultdict

def adjacentChars(s):
    heap = []
    res = []
    freq_map = defaultdict(int)
    
    for char in s:
        freq_map[char] -= 1  # use negative counts for max heap
    
    for char, freq in freq_map.items():
        heap.append((freq, char))
    
    heapq.heapify(heap)
    prev = None

    while heap or prev:
        if not heap and prev:
            # only one char left, and it can't be placed non-adjacently
            return None

        freq, char = heapq.heappop(heap)
        res.append(char)

        if prev:
            heapq.heappush(heap, prev)

        if freq + 1 != 0:
            prev = (freq + 1, char)
        else:
            prev = None

    return ''.join(res)

# Test case
print(adjacentChars("aaabbc"))  # Expected output like: "ababac"

