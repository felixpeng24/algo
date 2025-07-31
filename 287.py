"""
You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].


"""
from collections import defaultdict
import heapq

def topkwebsite(userList, k):
    userHash = defaultdict(set)
    for website, user in userList:
        userHash[website].add(user)

    def similarities(web1, web2):
        count = 0
        for user in userHash[web1]:
            if user in userHash[web2]:
                count += 1
        return count
    
    webList = [web for web in userHash.keys()]
    comboHeap = []

    for i in range(len(webList)):
        for j in range(i+1, len(webList)):
            heapq.heappush(comboHeap, (-similarities(webList[i], webList[j]), webList[i], webList[j]))
    
    res = []

    for _ in range(k):
        similarity, web1, web2 = heapq.heappop(comboHeap)
        res.append((web1, web2))
    
    return res

a = [('a', 1), ('a', 3), ('a', 5), ('b', 2), ('b', 6), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
b = 3
print(topkwebsite(a, b))
