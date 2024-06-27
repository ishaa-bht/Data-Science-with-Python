# #creating a set
# set1 = set()  #if used {} it becomes dictionary
# print(set1)
# print(type(set1))

# set2 = {1, 2 , 3, 4, 4 } # outputs only one 4
# print(set2)
# print(type(set2))

# #Adding element in set
# set2.add(5)
# print(set2)

# #Removing element from set
# set2.discard(1)
# print(set2)
# set2.remove(2)
# print(set2)
# set2.discard(2)
# print(set2)

#Operation on Set
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
intersection_set = set3.intersection(set4)
print(f"Intersection set: {intersection_set}")

union_set = set3.union(set4)
print(f"Union set: {union_set}")

difference_set = set.difference(set4)
print(f"Difference set: {difference_set}")

#Use case of set
list1 = ["Ram", "Haro", "Zita", "Sama"]
list2 = ["Haro", "Zita", "Gopal"]

set1= set(list1)
set2= set(list2)

common_names = set1.intersection(set2)
common_names = list(common_names)
print(f"Common names are: {common_names}")
