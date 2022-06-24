my_generator = (x for x in range(0,10))
zero = next(my_generator)
one = next(my_generator)
for rest_of_range in my_generator:
    print(rest_of_range)
print(zero)
print(one)
print(my_generator[2])
