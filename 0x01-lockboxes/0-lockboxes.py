#!/usr/bin/python3
"""Checks if a collection of boxes can be unlocked with keys
    found inside them."""


def canUnlockAll(containers):
    """Determines if all containers can be opened"""
    index = 0
    accessible = {}

    for container in containers:
        if len(container) == 0 or index == 0:
            accessible[index] = "always_open"
        for code in container:
            if code < len(containers) and code != index:
                accessible[code] = code
        if len(accessible) == len(containers):
            return True
        index += 1
    return False
