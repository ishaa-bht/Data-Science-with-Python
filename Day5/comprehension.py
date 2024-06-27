# list_of_num = [1, 2, 3, 4]
# list_of_square_of_num = []

# for n in list_of_num:
#     list_of_square_of_num.append(n*n)
# print(list_of_square_of_num)

# #Calculate square of number using List comprehension
# list_of_num = [1, 2, 3, 4]

# # list_of_square_of_num = [expression for item in sequence if condition]  #syntax
# list_of_square_of_num = [n**2 for n in list_of_num ]
# print(list_of_square_of_num)

# list_of_square_of_even_num = [n**2 for n in list_of_num if n % 2 == 0]
# print(list_of_square_of_even_num)

# #Set comprehension
# set1 = set()
# set_of_square_num = set()
# set1={1,2,3,4}

# for num in set1:
#     set_of_square_num.add(num**2)
# print(set_of_square_num)

# #With set comprehension

# set_of_square_num = {num**2 for num in set1}
# print(set_of_square_num)

# #without dictionary comprehension
# ori_dict = {"a" : 1, "b" : 2, "c" : 3}
# swappped_dict ={}
# for key,value in ori_dict.items():
#     swappped_dict[value] = key
# print(swappped_dict)

# #with dictionary comprehension
# # new_dict = {key: expression for item in sequence if condition}
# swappped_dict = { value: key for key,value in ori_dict.items() }
# print(swappped_dict)

# #store even values doing square
# even_values = {key:value**2 for key,value in ori_dict.items()  if value % 2 == 0}
# print(even_values)






