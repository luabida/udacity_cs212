# -----------
# User Instructions
# 
# Define a function, two_pair(ranks).

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pairs = []
    for r in ranks:
        if ranks.count(r) == 2:
            pairs.append(r)
    if len(set(pairs)) == 2:
        return (max(pairs), min(pairs))
    else:
        return None


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD 9H TH 9C 3S".split() # Two Pair
    p = "TD 9H TH 2C 3S".split() # Pair
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    pranks = card_ranks(p)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    print(two_pair(tpranks))
    assert two_pair(tpranks) == (10, 9)
    print(two_pair(pranks))
    assert two_pair(pranks) == None
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

print(test())
