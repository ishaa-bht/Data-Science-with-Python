# #creating an empty dictionary

# dict1 = {}
# print(dict1)
# print (type(dict1))

student = {
    "name" : "Isha",
    "age" : 19,
    "courses" : ["Maths", "Physics", "Chemistry"]

}
print(f"Student: {student}")

#Accessing elements in dictionart
#Accessing using keys
student_name = student["name"]
print(f"Name: {student_name}")

student_courses = student["courses"]
print(f"Student courses: {student_courses}")

#Accessing using get() method
student_name = student.get("name")
print(f"Name: {student_name}")

student_address = student.get("address", "Not available")
print(f"Address: {student_address}")

#Adding new item in the dictionary

student["address"] = "Bhaktapur"
print(f"Dictionary after adding address: {student}")

#Updating values
student["address"] = "Biratnagar"
print(f"Dictionary after changing address: {student}")

#Dictionary methods
#keys() method will return list of all the keys
student_keys = student.keys()
print(f"Keys: {student_keys}")

#values() method will return the list of all values
student_values = student.values()
print(f"Values: {student_values}")

#items() method will return the list of tuples and each tuples contains key value

student_items = student.items()
print(f"Items: {student_items}")

#Looping over key-value pairs
for key,value in student.items():
    # key,value = x #unpacking    
    print(f"{key}: {value}")

#Deleting an item from the dictionary
del student["address"]
print(f"Dictionary after deleting address: {student}")
    
#Looping over two lists of same length
list1 = [1,2,3]
list2 = [1,2,3]
for v1,v2 in zip(list1,list2): #v1 from list1 and v2 from list2
    print(v1*v2)
