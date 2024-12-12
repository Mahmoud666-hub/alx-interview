#!/usr/bin/python3
"""
Module prime_gamexx
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


def getPrime(intgers):
    """
    Returns a prime number
    from a set of intgers
    """
    for x in intgers:
        if isPrime(x):
            return x
    return None


def removePrimeNo(intgs, prim):
    """
    removes a prime number from a set
    """
    intgs.remove(prim)


def removeMultiples(ints, number):
    """removes multiples of a number"""
    for x in ints.copy():
        if (x % number) == 0:
            ints.remove(x)


def isWinner(m, nums):
    """
    Determines the winner
    """
    m_wins = 0
    b_wins = 0
    canPlay = True
    times = 0

    if not m or not nums:
        return None

    for n in nums:
        ints = set([n for n in range(1, n + 1)])
        player = "m"
        while times <= m:
            prime = getPrime(ints)

            if prime is None:
                if player == "m":
                    b_wins += 1
                else:
                    m_wins += 1
                break
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
