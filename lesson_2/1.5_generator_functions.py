## Generator Functions
'''
def ints(start, end):
    i = start
    while i <= end:
        yield i
        i += 1

l = ints(0, 100000)
for i in l:
    print(i)
'''
# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    
def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    l = ints(0,10)
    for n in l:
        yield n
        if n > 0:
            yield n - 2*n

for v in all_ints():
    print(v)


''' Incorrect. You didn't define all_ints as a generator function.

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    l = ints(0, 10)
    result = []
    for n in l:
        result.append(n)
        result.append(n - 2*n)
    result.remove(result[0])
    return ', '.join(str(n) for n in result)

print(all_ints())
'''
