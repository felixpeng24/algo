"""

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""

import random
from collections import defaultdict

def run_markov_chain(start, transitions, num_steps):
    # Organize the transitions into a dict of dicts for faster lookup
    transition_dict = defaultdict(list)
    for from_state, to_state, prob in transitions:
        transition_dict[from_state].append((to_state, prob))
    
    # Precompute cumulative probabilities for random.choices
    cumulative_transitions = {}
    for state, transitions in transition_dict.items():
        states, probs = zip(*transitions)
        cumulative_transitions[state] = (states, probs)

    current_state = start
    visit_counts = defaultdict(int)
    for _ in range(num_steps):
        visit_counts[current_state] += 1
        states, probs = cumulative_transitions[current_state]
        current_state = random.choices(states, probs)[0]

    return dict(visit_counts)

# Example usage
start_state = 'a'
num_steps = 5000
transitions = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

result = run_markov_chain(start_state, transitions, num_steps)
print(result)
