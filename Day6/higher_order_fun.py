# #Iterable and Iterator

# Iterable are those objects whose elements can be accessed using loop
# Examples: list, tuple, set, dictionary,String
# Iterables have methods like __iter__()

#Iterator
# Iterator are those objects which stores stream of data
# Iterator have methods like __iter__() and __next__()

# my_list=[1,2,3,4]
# #my_list is iterable because we can access its elements using loops
# for num in my_list:
#     print(num)

# #myList as a iterator
# my_iterator= iter(my_list)
# print(my_iterator)

# first_element = next(my_iterator)
# print(first_element)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# #converting iterator to list
# my_list= [1,2,3,4]
# new_iterator = iter(my_list)
# first_element=next(new_iterator) 
# print(first_element) 
# new_list = list(new_iterator)
# print(new_list)

#map function in python
#map is higher order function which takes two arguments viz
#1. function 
#2. iterable
#and applies the function to each element of the iterable
#and returns an iterator

#Usage: We use map function when we have to apply
# a fuction to each element of an iterable


# #write a function to calculate square of a number and use it to 
# #calculate square of numbers in a list

# def cal_squ(num):
#     return num**2

# my_list=[1,2,3,4]
# output_list=[]

# for num in my_list:
#     output_list.append(cal_squ(num))

# print(output_list)

# #COMPREHENSION

# squ=[cal_squ(n) for n in my_list]
# print(squ)

# squ_using_map_func = map(cal_squ, my_list)
# squ_using_map_func=list(squ_using_map_func)
# print(squ_using_map_func)

# #using lambda function inside map
# squ_with_map_lambda_func =list( map(lambda num: num**2, my_list))
# print(squ_with_map_lambda_func)

# #filter function
# #boolean
#     #it is similar to map function
#     #The function which we pass to filter function should return a boolean value
#     #filter function returns an iterator that contains only those elements
#     #for which the function returns true

# squ_with_filter_func = filter(cal_squ, my_list)
# squ_with_filter_func = list(squ_with_filter_func)
# print(squ_with_filter_func)

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else: 
#         return False
# input_list=[1,2,3,4,5,6,7]
# output_list_with_comprehension = [num for num in input_list if is_even(num)]
# print(f"Filtered even numbers: {output_list_with_comprehension}")

# output_with_filter_func = list(filter(is_even,input_list))
# print("Filtered even numbers with filter function:", output_with_filter_func)

# output_with_filter_func_lambda = list(filter(lambda num: num % 2 == 0, input_list))
# print("Filtered even numbers with filter lambda function:", output_with_filter_func_lambda)


#reduce function

#we have to add all the elements of a list

list1 = [1, 2, 3, 4, 5]

from functools import reduce
def add_two_numbers(num1,num2):
        return num1 + num2

cumulative_sum  = reduce(add_two_numbers,list1)
print(cumulative_sum)