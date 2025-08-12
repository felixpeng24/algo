"""
A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:

A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}


"""

import heapq
from collections import defaultdict

def mst_cost_and_edges(graph, start='plant'):
    # Make undirected adjacency list
    adj = defaultdict(dict)
    for u, nbrs in graph.items():
        for v, w in nbrs.items():
            adj[u][v] = min(adj[u].get(v, float('inf')), w)
            adj[v][u] = min(adj[v].get(u, float('inf')), w)

    visited = set([start])
    pq = []
    for v, w in adj[start].items():
        heapq.heappush(pq, (w, start, v))

    total = 0
    chosen = []

    while pq and len(visited) < len(adj):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        total += w
        chosen.append((u, v, w))
        for x, wx in adj[v].items():
            if x not in visited:
                heapq.heappush(pq, (wx, v, x))

    if len(visited) != len(adj):
        raise ValueError("Graph is not fully connectable from the plant.")

    return total, chosen

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}

total, edges = mst_cost_and_edges(pipes, start='plant')
print(total)  # 16
print(edges)  # e.g. [('plant','A',1), ('plant','B',5), ('B','C',10)]
