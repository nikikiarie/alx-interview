#!/usr/bin/python3
"""Calculate the minimum operations to reach target_count of A's
using only Copy All and Paste operations."""


def minOperations(target_count: int) -> int:
    """Find the minimum operations to get target_count A's in file"""
    divisor = 2
    operations = 0
    while target_count > 1:
        while target_count % divisor == 0:
            operations += divisor
            target_count /= divisor
        divisor += 1
    return operations
