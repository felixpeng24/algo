"""

Alice wants to join her school's Probability Student Club. 
Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. 
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program 
to simulate the two games and calculate their expected value.
"""

import random
import numpy as np

def simulate_game(target_pair, trials=100000):
    results = []
    for _ in range(trials):
        count = 0
        prev_roll = None
        while True:
            roll = random.randint(1, 6)
            count += 1
            if prev_roll == target_pair[0] and roll == target_pair[1]:
                break
            prev_roll = roll
        results.append(count)
    return np.mean(results)

# Simulate both games
expected_game_A = simulate_game((5, 6))
expected_game_B = simulate_game((5, 5))

print(expected_game_A)
print(expected_game_B)
