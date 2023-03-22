from typing import List


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


def max_profit_muliple_transactions(prices: List[int]):
    if __debug__:
        print(prices)

    min_price = prices[0]
    high = prices[0]
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < high:
            profit = max_profit_muliple_transactions(prices[i:])
            break
        
        else:
            high = max(high, prices[i])
        
    return profit + (high - min_price)
