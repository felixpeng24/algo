"""
A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.

"""

# def generate_subsets(s):
#     def backtrack(index, path):
#         if index == len(s):
#             print(''.join(path))
#             print("test")
#             return
#         # Exclude first
#         path.append(s[index])
#         backtrack(index + 1, path)
#         path.pop()
#         # Include
        
#         backtrack(index + 1, path)
        

#     backtrack(0, [])

def shortest_route(elevations, paths):
    from collections import defaultdict

    # Convert paths into adjacency list
    graph = defaultdict(list)
    for (u, v), d in paths.items():
        graph[u].append((v, d))
        graph[v].append((u, d))  # assuming undirected

    min_distance = [float('inf')] #made into an array since arrays are mutable; if it was a regular variable, copies inside dfs fucntion would be made instead

    def dfs(node, direction, dist, visited, switched):
        if node == 0 and switched and dist > 0:
            min_distance[0] = min(min_distance[0], dist)
            return

        for neighbor, edge_dist in graph[node]:
            if (neighbor, direction) in visited:
                continue

            elev_curr = elevations[node]
            elev_next = elevations[neighbor]

            # Decide next move based on direction and elevation
            if direction == 'start':
                if elev_next > elev_curr:
                    visited.add((neighbor, 'up'))
                    dfs(neighbor, 'up', dist + edge_dist, visited, switched)
                    visited.remove((neighbor, 'up'))
            elif direction == 'up':
                if elev_next > elev_curr:
                    visited.add((neighbor, 'up'))
                    dfs(neighbor, 'up', dist + edge_dist, visited, switched)
                    visited.remove((neighbor, 'up'))
                elif elev_next < elev_curr:
                    visited.add((neighbor, 'down'))
                    dfs(neighbor, 'down', dist + edge_dist, visited, True)
                    visited.remove((neighbor, 'down'))
            elif direction == 'down':
                if elev_next < elev_curr:
                    visited.add((neighbor, 'down'))
                    dfs(neighbor, 'down', dist + edge_dist, visited, switched)
                    visited.remove((neighbor, 'down'))

    # Start DFS from node 0
    dfs(0, 'start', 0, set(), False)

    return min_distance[0] if min_distance[0] != float('inf') else -1
