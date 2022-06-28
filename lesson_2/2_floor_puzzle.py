#------------------
# User Instructions
"""
Hopper, Kay, Liskov, Perlis, and Ritchie live on 
different floors of a five-floor apartment building. 

Hopper does not live on the top floor. 
Kay does not live on the bottom floor. 
Liskov does not live on either the top or the bottom floor. 
Perlis lives on a higher floor than does Kay. 
Ritchie does not live on a floor adjacent to Liskov's. 
Liskov does not live on a floor adjacent to Kay's. 

Where does everyone live?  
""" 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools as it

def floor_puzzle():
    apts = [bottom, _, _, _, top] = [1,2,3,4,5]
    orderings = list(it.permutations(apts))
    return list(next((Hopper, Kay, Liskov, Perlis, Ritchie) 
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if Hopper is not top
                if Kay is not bottom
                if Liskov is not top
                if Liskov is not bottom
                if hi(Perlis, Kay)
                if not adj(Ritchie, Liskov)
                if not adj(Liskov, Kay)))

def adj(apt1, apt2):
    return abs(apt1-apt2) == 1

def hi(apt1, apt2):
    return apt1 > apt2

def lo(apt1, apt2):
    return apt1 < apt2
