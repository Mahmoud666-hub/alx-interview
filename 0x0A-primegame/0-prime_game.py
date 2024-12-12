#!/usr/bin/python3
"""
Module 0-prime_game
"""


def isPrime(numb):
    """
    checks if a numb
    is a prime number
    """
    if numb < 2:
        return False
    for i in range(2, numb):
        if (numb % i) == 0:
            return False
    return True


def getPrime(ints):
    """
    Returns a prime number
    from a set
    """
    for a in ints:
        if isPrime(a):
            return a
    return None


def removePrimeNo(ints, prime):
    """
    removes a prime number from a set
    """
    ints.remove(prime)


def removeMultiples(ints, number, player):
    """removes multiples of a number"""
    for x in ints.copy():
        if (x % number) == 0:
            # print(f"{player} removes {x}")
            ints.remove(x)


def isWinner(x, nums):
    """
    Determines the winner
    """
    m_wins = 0
    b_wins = 0
    canPlay = True
    times = 0

    if not x or not nums:
        return None

    for n in nums:
        ints = set([n for n in range(1, n + 1)])
        player = "m"
        while times <= x:
            prime = getPrime(ints)
            # A win for the other player
            # when no more prime numbers exist
            # print(f"{player} picks {prime}")
            if prime is None:
                if player == "m":
                    b_wins += 1
                else:
                    m_wins += 1
                break
            # remove prime number
            # print(f"{player} removes {prime}")
            removePrimeNo(ints, prime)
            removeMultiples(ints, prime, player)

            if player == "b":
                player = "m"
            else:
                player = "b"
            times += 1
        times = 0

    if m_wins == b_wins:
        return None
    return "Maria" if m_wins > b_wins else "Ben"