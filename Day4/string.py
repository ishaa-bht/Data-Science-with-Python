# string1 = 'Hello World'
# print(string1)

# string2 = "Hello World"
# print(string2)

# #Accessing characters in a string
# first_char = string1[0]
# last_char = string1[-1]
# print(f"First character: {first_char}  \nLast Character: {last_char}")

# #looping over string
# for char in string1:
#     print(char)

# #String concatenation
# str1 = "Hello"
# str2 = "World"
# str3 = str1 + " " + str2
# print(str3)

#String Slicing
str4 = "Hello World"
print(str4[:])
print(str4[:5])
print(str4[: : -1])
print(str4[6:])

#String method
#split()
str5 = "Hello World"
list1 = str5.split() #delimter is by default space
print(list1)
list1 = str5.split('o') #delimeter is o
print(list1)

#strip()
str6 = "   Hello World  " #removes the white spaces at front and back
str7 = str6.strip()
print(str7)

#upper() and lower()
print(str7.upper())
print(str7.lower())


