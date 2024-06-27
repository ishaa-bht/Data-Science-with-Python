# #Syntax of for loop
# sequence = []
# for item in sequence:
#     #body of for loop
#     pass

# fruits = ["apple", "mango", "banana"]
# for fruit in fruits:
#     print(fruit)
 
#  #range() function returns the sequence of values within the range

# for i in range(len(fruits)):
#     print(i)

# #break statement

# for i in range(10): 
#     if i == 5:
#         break
#     print(i)

# #continue statement 
# for i in range(10): 
#     if i == 5:
#         continue
#     print(i)


#ennumerate() function
fruits = ["apple", "mango", "orange"]

for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")


