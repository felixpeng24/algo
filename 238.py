"""
This problem was asked by MIT.

Blackjack is a two player card game whose rules are as follows:

The player and then the dealer are each given two cards.
The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
The dealer must then hit if their total is 16 or lower, otherwise pass.
Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.
For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.

Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).

"""

def blackjack_solver(deck):
    n = len(deck)
    memo = {}

    def dfs(index, player_total, dealer_total, player_done):
        key = (index, player_total, dealer_total, player_done)
        if key in memo:
            return memo[key]

        if player_total > 21:
            return -1  # player busts

        # Player's turn
        if not player_done:
            if index >= n:
                return -1  # no cards left to draw

            # Option 1: Hit
            hit = dfs(index + 1, player_total + deck[index], dealer_total, False)

            # Option 2: Stand
            stand = dfs(index, player_total, dealer_total, True)

            memo[key] = max(hit, stand)
            return memo[key]

        # Dealer's turn (player is done)
        dealer_total_now = dealer_total
        i = index
        while i < n and dealer_total_now < 17:
            dealer_total_now += deck[i]
            i += 1

        if dealer_total_now > 21:
            result = 1  # dealer busts
        elif player_total > dealer_total_now:
            result = 1
        elif player_total < dealer_total_now:
            result = -1
        else:
            result = 0  # tie

        memo[key] = result
        return result

    # Initial cards
    if n < 4:
        return 0  # not enough cards to play

    player_start = deck[0] + deck[2]
    dealer_start = deck[1] + deck[3]

    return dfs(4, player_start, dealer_start, False)
