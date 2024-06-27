# # creating a list

# myList = [] #empty list
# print(myList)
# print(type(myList))

# fruits = ["mango" , "apple", "orange" , "banana"]
# print(f"Length of fruits list is: {len(fruits)}")

# # Adding an element in list

# fruits.append ("papaya")
# print(f"Fruits after appending papaya: {fruits} ")

# fruits.insert(0,"litchi")
# print(f"Fruits after inserting litchi at first position : {fruits}")

# # Removing an element from the list
# popped_element = fruits.pop()  #returns a value,removes the last element of the list
# print(f"Popped element is: {popped_element}")
# print(f"List of fruits after popping: {fruits}")

# popped_element = fruits.pop()
# print(f"Popped element is: {popped_element}")
# print(f"List of fruits after popping: {fruits}")

# fruits.remove("apple")  #doesnot return a value, removes the specified element
# print(f"List of fruits after removing apple: {fruits}")

#Concatenation of list

list1 = [1,2,3]
list2 = [4,5,6]

concatenated_list = list1 + list2
print(f"Concatenated List: {concatenated_list} ")

#concatenation using extend function

list3 = [1,2,3]
list4 = [4,5,6]

list3.extend(list4) #cheaper operation computaionally
print(f"List3: {list3}")

#Slicing in List
list5 = [1, 2, 3, 4, 5]
first_element = list5[0]
second_element = list5[1]
sublist = list5[1:4:2]  #from 1 to 4 with step size 2
print(f"Sublist: {sublist}")

#Negative Indexing
last_element = list5[-1]
print(f"Last element: {last_element}")

second_last_element = list5[-2]
print(f"Second last element: {second_last_element}")

sublist1 = list5[-3: 4] #third last and fourth
print(f"Sublist1: {sublist1}")

reversed_list = list5[::-1]
print(f"Reversed list: {reversed_list}")

#Nested list
nested_list = [[1,2,3], [4,5,6], 7]
first_element = nested_list[0]
print(f"Nested list: {nested_list}")
print(f"First element of nested list: {first_element}")
print(nested_list[0][0])
print(nested_list[1][1])


