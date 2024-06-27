#creating tuple
tuple1 = () #empty tuple
print(tuple1)
print(type(tuple1))

tuple2 = ("Ram", 25 ,50)
first_element = tuple2[0]
last_element = tuple2[-1]
print (f"first element: {first_element}")
print(f"last element: {last_element}")
print(f"First two elements of tuple: {tuple2[:2]}")

 
# tuple2[0] = "Hari"  #shows error because tuple cannot be changed.
# print(f"new tuple: {tuple2}")

for item in tuple2:
    print(item)