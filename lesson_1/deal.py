# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.

from random import shuffle

mydeck = [r + s for r in "23456789TJQKA" for s in "SHDC"]


def deal(numhands, n=5, deck=mydeck):
    shuffle(deck)
    return [deck[n * h : n * (h + 1)] for h in range(numhands)]


print(deal(3, 5, mydeck))
# expected output:
# deal(3, 5, mydeck) = [[0:5],[5:10],[10:15]]
