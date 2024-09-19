#!/usr/bin/python3
"""
Change making module
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins for a given total.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    try:
        match_exact = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    total_coins = 0
    for j in coins:
        if total % j == 0:
            total_coins += total // j
            return total_coins
        if total - j >= 0:
            if total // j > 1:
                total_coins += total // j
                total = total % j
            else:
                total_coins += 1
                total -= j
                if total == 0:
                    break
    if total > 0:
        return -1
    return total_coins
