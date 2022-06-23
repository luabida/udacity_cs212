# -----------
# User Instructions
#
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10,
# 'J' to 11, etc...


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r, s in cards]
    figures = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    formated_ranks = []
    for rank in ranks:
        if rank in figures:
            formated_ranks.append(figures[rank])
        else:
            formated_ranks.append(int(rank))
    formated_ranks.sort(reverse=True)
    return formated_ranks


print(card_ranks(["AC", "3D", "4S", "KH"]))  # should output [14, 13, 4, 3]
