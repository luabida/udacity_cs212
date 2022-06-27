ta_data = [
    ("Peter", "USA", "CS262"),
    ("Andy", "USA", "CS212"),
    ("Sarah", "England", "CS101"),
    ("Gundega", "Latvia", "CS373"),
    ("Job", "USA", "CS387"),
    ("Sean", "USA", "CS253"),
]


# Expected output:
# A list of formated strings excluding those who live in USA

lc = [f"{n} lives in {c} and is the TA for {ta}" 
        for n, c, ta in ta_data 
        if c != "USA"
        ]

for sentence in lc:
    print(sentence)
