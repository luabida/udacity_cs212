ta_data = [
    ("Peter", "USA", "CS262"),
    ("Andy", "USA", "CS212"),
    ("Sarah", "England", "CS101"),
    ("Gundega", "Latvia", "CS373"),
    ("Job", "USA", "CS387"),
    ("Sean", "USA", "CS253"),
]


# Solution in LC:
# Expected output:
# Peter lives in USA and is the TA for CS262 ...

lc = [f"{n} lives in {c} and is the TA for {ta}" for n, c, ta in ta_data]
for sentence in lc:
    print(sentence)
