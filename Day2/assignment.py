#Average marks
# marks = [10,20,30,40,50,60]
# sum = 0
# avg = 0
# for mark in marks:
#     sum = sum + mark

# avg = sum/len(marks)

# print(f"Average Mark: {avg}")

# #Multiplication table of number given by user
# num = input("Enter the number to generate its multiplication table: ")
# num = int(num)
# for i in range(1,11,1):
#     mul = num * i
#     print(f"{num} * {i} = {mul} ")


# #Palindrome of a number
# num = input("Enter any number: ")
# str_num = str(num)
# num1 = str_num[::-1]

# palindrome = True if num1 == num else False
# print(palindrome)

# #Find greatest number
# list = [ 3, 5, 9, 7 ]
# greatest = list[0]

# for num in list :
   
#     if greatest < num:
#         greatest = num

# print(f"Greatest number in the list is: {greatest}")


#Peak element

# list = [ 3, 2, 6, 8, 1, 5, 4 ]

# peak = [] 
# for i in range(1, len(list) -1 , 1):
#     if list[i] > list[i+1] and list[i] > list[i-1] : 
        
#         peak.append(list[i])
        
# print(f"Peak elements are: {peak}")

#Count the number of vowels in a string

# str = input("Enter a string: ")
# vowel=["a","e" ,"i" ,"o" ,"u","A","E","I","O","U"]
# count = 0

# #print(str)
# for s in str:
#     for i in range(len(str)):
#         if s == vowel[i]:
#             count = count + 1

# print(f"Number of vowel: {count}")

# #Alternative
# vowels=aeiouAEIOU
# for s in str:
#     if s in vowels:
#         count = count + 1
# printf(f"Vowel count= {count}")

# #Sum of digits in an integer
# digit = input("Enter any digit")
# digit = str(digit)
# sum = 0

# for d in digit:
#     print(d)
#     d=int(d)
#     sum=sum+d

# print(f"Sum of digits: {sum}")

# #Convert Roman numeral to integer
# roman = input("Enter roman numeral: ")
# integer = 0

# def get_value(char):
#     if char == 'I':
#         return 1
#     elif char == 'V':
#         return 5
#     elif char == 'X':
#         return 10
#     elif char == 'L':
#         return 50
#     elif char == 'C':
#         return 100
#     elif char == 'D':
#         return 500
#     elif char == 'M':
#         return 1000
#     return 0




# for i in range(len(roman)-1):
#     current_value = get_value(roman[i])
#     next_value = get_value(roman[i+1])

#     if current_value < next_value:
#          integer = integer - current_value

#     else:
#         integer = integer + current_value


# integer = integer + get_value(roman[-1])

# print(integer)

# #Valid Paranthesis

# def paraCheck( seq ):
#     while True:
#         if '()' in seq :
#             seq = seq.replace('()', '')
#         elif '{}' in seq:
#             seq = seq.replace ('{}', '')
#         elif '[]' in seq:
#             seq = seq.replace ('[]', '')
#         else:
#             return not seq

# seq = input("Enter any parenthesis to check for validity: ")
# print(f"Is {seq} valid?: {paraCheck(seq)}")

# #Calculate frequency of characters

# str = input("Enter any string")
# output_dict = {}

# for s in str:
    
#     if s in output_dict.keys():
        
#         output_dict[s] = output_dict[s] + 1
#     else:
#         output_dict[s] = 1

# print(output_dict)



# grades_dict = {
#         "Alice": {"Math": 90, "Science": 85, "Literature": 88},
#         "Bob": {"Math": 78, "Science": 82, "Literature": 80},
#         "Charlie": {"Math": 92, "Science": 91, "Literature": 94}
# }

# for keys, value in grades_dict.items():
#     print(keys, value)
#     total = 0
#     for k,v in value.items():
#         total = total + v
#     print(f"Total marks: {total}")
#     percentage = (total/300)*100
#     print(f"Percentage of {keys} : {percentage}")

# #function

# def plusOne(digits):
#     n = len(digits)
    

#     for i in range(n - 1, -1, -1):
#         digits[i] += 1
        
        
#         if digits[i] < 10:
#             return digits
        
        
#         digits[i] = 0
    
    
#     return [1] + digits

# print(plusOne([1, 2, 3]))  
# print(plusOne([4, 3, 2, 1]))  
# print(plusOne([9])) 


# #Decorator

# timeit_decorator()







    
    
        


    


     

    


















