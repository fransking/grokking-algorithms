from grokking_algorithms.misc import max_profit
from grokking_algorithms.misc import max_profit_multiple_transactions


def test_max_profit_empty_list():
    result = max_profit([])
    assert result == (0, None, None)


def test_max_profit_one_price():
    result = max_profit([5])
    assert result == (0, None, None)


def test_max_profit_two_prices():
    result = max_profit([3, 5])
    assert result == (2, 0, 1)


def test_max_profit_only_losses():
    result = max_profit([5, 4, 3, 2, 1])
    assert result == (0, None, None)


def test_max_profit():
    prices = [7, 1, 5, 3, 6, 4]

    result = max_profit(prices)
    assert result == (5, 1, 4)  # buy day 2 sell day 5 for profit of 5 (6 - 1)


def test_max_profit_multiple_transactions():
    prices = [7, 1, 5, 3, 6, 4]

    # partition on each drop, recurse each right sublist of the partition
    # [7, 1, 5, 3, 6, 4] -> [(7), (1, 5), (3, 6, 4)] -> [0, 4, 3, 0] 

    result = max_profit_multiple_transactions(prices)
    assert result == 7  # buy day 2 sell day 3 for profit of 4, then buy day 4 and sell day 5 for profit of 3 == 7
