"""
A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.

"""

#what if we just add everyone, two for loops, one for each person, one for each person's friend
#ending would be
"""
create a set 


"""

def friendgroups(friendHash):
    visited = set()
    groups = 0
    
    def dfs(friend):
        for val in friendHash[friend]:
            if val not in visited:
                visited.add(val)
                dfs(val)

    for key in friendHash.keys():
        if key not in visited:
            groups += 1
            visited.add(key)
            dfs(key)

    return groups

# def friendgroupsBFS(friendHash):
#     visited = set()
#     groups = 0
#     q = []
#     for key in friendHash():
#         if key not in visited:
#             visited.add(key)
#             groups += 1
#             for friends in friendHash[key]
#                 if friends not in visited:
#                     visited.add(friends()

from collections import deque

def get_friend_groups(adj_list):
    visited = set()
    friend_groups = []

    for student in adj_list:
        if student not in visited:
            group = set()
            queue = deque([student])
            visited.add(student)

            while queue:
                current = queue.popleft()
                group.add(current)
                for neighbor in adj_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            friend_groups.append(group)
    
    return friend_groups


print(friendgroups({0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} ))