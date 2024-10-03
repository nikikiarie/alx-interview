#!/usr/bin/python3
"""Prime Game """


def isWinner(rounds, num_list):
    """rounds - number of rounds
    num_list - list of numbers
    """
    if rounds <= 0 or num_list is None:
        return None
    if rounds != len(num_list):
        return None

    benScore = 0
    mariaScore = 0

    primes = [1 for _ in range(sorted(num_list)[-1] + 1)]
    primes[0], primes[1] = 0, 0
    for idx in range(2, len(primes)):
        mark_multiples(primes, idx)

    for n in num_list:
        if sum(primes[0:n + 1]) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1

    if benScore > mariaScore:
        return "Ben"
    if mariaScore > benScore:
        return "Maria"
    return None


def mark_multiples(primes_list, index_prime):
    """Marks multiples
    of prime numbers
    """
    for multiple in range(2, len(primes_list)):
        try:
            primes_list[multiple * index_prime] = 0
        except (ValueError, IndexError):
            break
