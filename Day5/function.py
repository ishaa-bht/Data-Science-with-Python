# def function_name(list_of_parameters):
#     #body
#     pass
#     #return value

# #function to add two numbers

# def add_two_numbers(num1, num2=10):
#     #docstring 
#     """"
#     This function adds two numbers

#     Arguments: 
#         num1:first number
#         num2:second number

#     Return:
#         sum of num1 and num2
#     """

#     sum = num1 + num2
#     return sum

# #Function call
# sum = add_two_numbers(10, 20) #positional arguments
# print(f"sum: {sum}")

# #keyword arguments
# sum = add_two_numbers(num1=10, num2=20) #can be used in any order
# print(f"sum: {sum}")

# #using default arguments
# sum = add_two_numbers(30) #num1=30
# print(f"sum: {sum}")

# #Unpacking of list,tuple
# list1 =[10, 20, 30, 40, 50]
# # x=list1[0]
# # y=list1[1]
# # z=list1[2]

# # x,y,z = list1  

# # print(x,y,z)

# #We can use * operator to unpack sequence
# x, *y, z = list1  #y holds multiple values
# print(x,y,z)

add = 10
def sum_num(*args):  #holds multiple arguments
    sum = 0
    add = 0
    print(args)
    print(add)
    for value in args:
        sum = sum + value
    return sum

print(add)
result = sum_num()
print(result)


#**kwargs in python
#**kwargs is used to pass arbitary number of keyword arguments #dictionary 
#*whereas *args is used to pass arbitrary number of positional arguments #tuple

def student_details(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")

student_details(name="Isha", age=20, address ="Bhaktapur", course="Python")


def student_dets(name, *args, **kwargs):
    #here required parameter is name only, other two is optional
    print(name)
    print(args)
    print(kwargs)
student_dets("Isha", 20, "Bhaktapur", course="Python")

#lambda function
#called anonymous funcion because it has no name

#syntax
    # lambda arguments: expression
    # lambda arguments: value if condition else else_value


def square(num):
    return num**2
square_of_10 = square(10)
print(square_of_10)

#Using lambda function
square = lambda num : num**2
square_of_10 = square(10)
print(square_of_10)

#square of even numbers and cube of odd numbers using lambda

square_cube = lambda num: num**2 if num%2 == 0 else num**3

result = square_cube(5)
print(result)
print(square_cube(4))




