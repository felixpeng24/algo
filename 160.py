r"""
Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, 
the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.

"""

#first reaction: dfs each branch, then choose two branches and go through root)

from collections import defaultdict

def find_farthest(node, graph, visited):
    stack = [(node, 0)]  # (current node, current distance)
    farthest_node, max_distance = node, 0
    visited[node] = True

    while stack:
        current, dist = stack.pop()
        if dist > max_distance:
            max_distance = dist
            farthest_node = current
        
        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append((neighbor, dist + weight))
    
    return farthest_node, max_distance

def longest_path_in_tree(edges):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Since it's an undirected tree

    # Step 1: Start DFS from an arbitrary node (first node in edges)
    start_node = edges[0][0]
    visited = defaultdict(bool)
    farthest, _ = find_farthest(start_node, graph, visited)

    # Step 2: Run DFS from this farthest node to find actual longest path
    visited = defaultdict(bool)
    _, longest_path = find_farthest(farthest, graph, visited)

    return longest_path

# Example usage:
edges = [
    ('a', 'b', 3), ('a', 'c', 5), ('a', 'd', 8),
    ('d', 'e', 2), ('d', 'f', 4), ('e', 'g', 1), ('e', 'h', 1)
]

print(longest_path_in_tree(edges))  # Output: 17
