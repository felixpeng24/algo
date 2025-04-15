"""
 Implement rand7() — which returns a uniform random integer from 1 to 7 — 
 using only a rand5() function (which returns a uniform integer from 1 to 5).
"""

# generate one through 25 evenly

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        row = rand5() - 1
        col = rand5() - 1
        num = row * 5 + col + 1  # Gives 1 to 25
        if num <= 21:
            return (num - 1) % 7 + 1
