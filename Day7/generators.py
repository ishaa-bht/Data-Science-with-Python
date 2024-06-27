#generator definition, uses yield
def myGenerator(num):
    for i in range(num):
        yield i

#calling generator function
myIterator = myGenerator(5)
print(myIterator)

#accessing generator element using next() method

print(next(myIterator))
print(next(myIterator))

#accessing generator element using for loop
for num in myIterator:
    print(f"Using for loop: {num}")

#creating generator using generator expression
myGenerator_from_gen_expr = (i for i in range(5))
for val in myGenerator_from_gen_expr:
    print(f"Using generator expression: {val}")




