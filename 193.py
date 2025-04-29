"""
Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many 
transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9,
 since you could buy the stock at 1 dollar, and sell at 8 dollars, and 
 then buy it at 4 dollars and sell it at 10 dollars. Since we did two 
 transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit
minus 4 dollars of fees.

"""

#O(n^2) solution with checking each value 
#sliding window? then pop largest value to find second largest max profit?

def max_profit_with_fee(prices, fee):
    if not prices:
        return 0

    n = len(prices)
    cash = 0           # Profit if we do not hold a stock
    hold = -prices[0]  # Profit if we hold a stock (start by buying first stock)

    for price in prices[1:]:
        # Decide whether to sell today
        cash = max(cash, hold + price - fee)
        # Decide whether to buy today
        hold = max(hold, cash - price)

    return cash

# Example usage:
print(max_profit_with_fee([1, 3, 2, 8, 4, 10], 2))  # Output: 9

#this is insanity what
"""
Day 1 (price = 3):

Sell? hold + price - fee = (-1) + 3 - 2 = 0

So cash = max(cash, hold + price - fee) = max(0, 0) = 0

Buy? cash - price = 0 - 3 = -3

hold = max(hold, cash - price) = max(-1, -3) = -1

→ Result: cash = 0, hold = -1

-----

Day 2 (price = 2):

Sell? hold + price - fee = (-1) + 2 - 2 = -1

cash = max(0, -1) = 0

Buy? cash - price = 0 - 2 = -2

hold = max(-1, -2) = -1

→ Result: cash = 0, hold = -1

--------

Day 3 (price = 8):

Sell? hold + price - fee = (-1) + 8 - 2 = 5

cash = max(0, 5) = 5

Buy? cash - price = 5 - 8 = -3

hold = max(-1, -3) = -1

→ Result: cash = 5, hold = -1

(Sold for a profit! +5 cash)

-------

Day 4 (price = 4):

Sell? hold + price - fee = (-1) + 4 - 2 = 1

cash = max(5, 1) = 5

Buy? cash - price = 5 - 4 = 1

hold = max(-1, 1) = 1

→ Result: cash = 5, hold = 1

(Bought again at 4)

----------

Day 5 (price = 10):

Sell? hold + price - fee = (1) + 10 - 2 = 9

cash = max(5, 9) = 9

Buy? cash - price = 9 - 10 = -1

hold = max(1, -1) = 1

→ Result: cash = 9, hold = 1

(Sold for another profit! +4 more cash)

✅ Final answer:

cash = 9
"""
