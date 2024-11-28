#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, amount):
    """
    How many of this type of coin can I get with my money?
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        numb = amount // coin
        amount -= numb * coin
        count += numb
    return count if amount == 0 else -1
