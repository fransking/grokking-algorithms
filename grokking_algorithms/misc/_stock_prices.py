from grokking_algorithms.collections import Heap

from typing import List
from math import floor


def max_profit(prices: List[int]) -> tuple:
    """
    Returns max profit plus the indices of the day to buy and subsequently sell to realise that profit
    """
    if len(prices) <= 1:
        return 0, None, None

    buy_index = 0
    sell_index = None

    min_price = prices[0]
    max_profit = 0

    for i in range(len(prices) - 1):
        current_min_price = min_price
        current_max_profit = max_profit

        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i + 1] - min_price)

        if min_price < current_min_price:
            buy_index = i

        if max_profit > current_max_profit:
            sell_index = i + 1

    return (max_profit, buy_index, sell_index) if max_profit > 0 else (0, None, None)


def max_profit_multiple_transactions(prices: List[int]):
    if __debug__:
        print(prices)

    min_price = prices[0]
    high = prices[0]
    profit = 0

    for i in range(len(prices)):
        if prices[i] < high:
            profit = max_profit_multiple_transactions(prices[i:])
            break
        
        else:
            high = max(high, prices[i])
        
    return profit + (high - min_price)


def max_profit_n_transactions(prices: List[int], num_buy_sells=1):
    if num_buy_sells < 0:
        raise ValueError("Must have at least one buy and sell")
    
    if num_buy_sells == 0:
        return 0

    n_largest_profits = []
    profits = Heap()

    def _max_profit(slice: List[int]):

        if __debug__:
            print(slice)
            
        min_price = slice[0]
        high = slice[0]

        for i in range(len(slice)):
            if slice[i] < high:
                _max_profit(slice[i:])
                break

            else:
                high = max(high, slice[i])
            
        profit = high - min_price

        if profit > 0:
            # assuming smaller values of num_buy_sells, cap the heap at this size
            # popping the largest element if it is exceeded
            n_largest_profits.extend(profits.insert(profit, cap=num_buy_sells))

    _max_profit(prices)

    # extend n_largest_profits to required numver of buys and sell
    remainder = num_buy_sells - len(n_largest_profits)
    n_largest_profits.extend(profits.take(remainder))

    return sum(n_largest_profits)
