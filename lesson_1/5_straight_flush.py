# -----------
# User Instructions
#
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.


def straight(ranks) -> bool:
    "Return True if the ordered ranks form a 5-card straight."
    ranks_s = sorted(ranks)
    avg = int(sum(ranks) / 5)
    if avg == ranks_s[2]:
        return True
    return False


def flush(hand) -> bool:
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    suits_rank = {"D": 1, "S": 2, "H": 3, "C": 4}
    suits_form = []
    for suit in suits:
        suits_form.append(suits_rank[suit])
    avg = int(sum(suits_form) / 5)
    if avg == suits_rank[suit]:
        return True
    return False


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    f = "TD 2D 5D 7D QD".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert straight([2, 6, 3, 4, 5]) == True
    assert flush(f) == True
    assert flush(sf) == True
    assert flush(fk) == False
    return "tests pass"


print(test())
