"""
Currency Conversion Problem

Parameters:
* rates: list of lists, where each sublist is [from_currency, to_currency, rate]
  Example: ['USD', 'GBP', 0.77] means 1 USD = 0.77 GBP
* goal: list containing [from_currency, to_currency]

Return: conversion rate from goal[0] to goal[1]

Example:
rates = [
    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]
goal = ['GBP', 'AUD']
Expected output: 1.89

Explanation: GBP -> JPY (1/0.0070) -> USD (1/110) -> AUD (1.45)
= 142.857 * 0.00909 * 1.45 ≈ 1.89
"""

from collections import defaultdict

def convertCurrDFS(rates, goal):
    #Building the graph
    currGraph = defaultdict(list)
    for rate in rates:
        currGraph[rate[0]].append([rate[1], rate[2]])
        currGraph[rate[1]].append([rate[0], (1/rate[2])])
    
    def dfs(visited, node, value):
        if node[0] == goal[1]:
            return value*node[1]
        
        visited.add(node[0])

        for currency in currGraph[node[0]]:
            #currGraph[node] = [$, val], [$, val]
            if currency[0] not in visited:
                result = dfs(visited, currency, value*node[1])
                if result is not None:
                    return result
    
    return dfs(set(), [goal[0], 1], 1)

from collections import deque
def convertCurrBFS(rates, goal):
    #Building the graph
    currGraph = defaultdict(list)
    for rate in rates:
        currGraph[rate[0]].append([rate[1], rate[2]])
        currGraph[rate[1]].append([rate[0], (1/rate[2])])
    
    q = deque([[goal[0], 1]])
    visited = set()

    while q:
        curr = q.popleft()

        visited.add(curr[0])
        if curr[0] == goal[1]:
            return curr[1]
        
        for currency in currGraph[curr[0]]:
            #currGraph[node] = [$, val], [$, val]
            if currency[0] not in visited:
                q.append([currency[0], currency[1]*curr[1]])
            
    return None
        



    
rates = [
    ['USD', 'JPY', 110],
    ['USD', 'AUD', 1.45],
    ['JPY', 'GBP', 0.0070]
]
goal = ['GBP', 'AUD']

print(convertCurrDFS(rates, goal))