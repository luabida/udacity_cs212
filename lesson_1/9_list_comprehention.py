udacity_tas = ["Peter", "Andy", "Sarah", "Gundega", "Job", "Sean"]

bad_uppercase_tas = []
for i in range(len(udacity_tas)):
    bad_uppercase_tas.append(udacity_tas[i].upper())

print(bad_uppercase_tas)

# Solution in List Comprehention:

uppercase_tas = [i.upper() for i in udacity_tas]


def test():
    assert uppercase_tas == ["PETER", "ANDY", "SARAH", "GUNDEGA", "JOB", "SEAN"]
    print("Tests Passed!")


print(test())
