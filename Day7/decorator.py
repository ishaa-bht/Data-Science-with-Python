# #PASSING FUNCTION AS AN ARGUMENT TO ANOTHER FUNCTION

# def function1():
#     print("Hello from function 1. ")

# def function2(func):
#     print("Hello from function 2")
    
    
#     func()

# function2(function1)

# #Returning function from another function

# def outer_func():
#     print("Hello from outer function")

#     def inner_function():
#         print("Hello from inner function")
    
#     return inner_function
# func_var= outer_func()
# func_var()

#Decorator in Python
# import math
# def square_root(num):
#     sq_root = math.sqrt(num)
#     return sq_root

# def decorator_positive_num_only(original_func):
#     def wrapper(num):
#         if num < 0:
#             print("Only positive numbers are allowed")
#             raise ValueError
#         else:
#             sq_root = original_func(num)
#             return sq_root
    
#     return wrapper

# #Using a decorator
# new_decorated_func = decorator_positive_num_only(square_root)
# print(new_decorated_func(9))
# # print(new_decorated_func(-9))

# #Shorthand notation to use decorator
# @decorator_positive_num_only
# def area_of_square_land(length):
#     area = length**2
#     return area

# # new_area_decorator_func = decorator_positive_num_only(area_of_square_land)

# # print(f"Area of lan with lenth 10: {new_area_decorator_func(10)}")
# # print(f"Area of lan with lenth 10: {new_area_decorator_func(-10)}")

# print(f"Area of land with length 9: {area_of_square_land(9)}")

#Custom timeit decorator
import time
def timeit(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        stop= time.time()
        print(f"Execution time of function: {stop} - {start} seconds")
    
    return wrapper
@timeit
def num_generator(num):
    for i in range(num):
        print (i)

num_generator(10)

@timeit
def sum_of_list(input_list):
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum

input_list = [1,2,3,4,5]
sum_of_list(input_list)

