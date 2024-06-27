class Book:
    #Attribute or properties section
    #In this section we will define the state/properties of the object
    class_variable = "I am a class variable"

    #Constructor
    def __init__(self,title, author_name, price, discount_rate):
        #Usage: USed for initialization of object properties
        self.title = title
        self.author = author_name
        self.price = price
        self.discount = discount_rate
    
        print("I am constructor of BOOK CLASS:",self)

    #Behaviour or methods section
    def calculate_sp(self):
        self.sp= self.price - (self.price * self.discount / 100 )
        # return sp
    
# #Instantiating the class or creating an object of the class
# book1 = Book(title="Harry Potter",author_name="JK Rowling",price=450,discount_rate=20)
# book2 = Book("Python","Ryan Reynolds",700,10)

# #Accessing object attributes
# #we can access object attributes and methods using dot(.) operator

# print(book1.title)
# print(book1.author)
# print(book1.price)
# print(book1.discount)
# print(book1.class_variable)
# print(book2.title)
# print(book1.class_variable)

# book1.calculate_sp()
# print("Selling price of book1: ",book1.sp)

# book2.calculate_sp()
# print("Selling price of book2: ", book2.sp)

# #Create a class RECTANGLE and find perimeter and area

# class Rectangle:

#     def __init__(self, rect_length, rect_breadth):
#         self.length =  rect_length
#         self.breadth = rect_breadth
#         self.area = 0
#         self.perimeter = 0

#     def calculate_area(self):
#         self.area = self.length * self.breadth

#     def calculate_perimeter(self):
#         self.perimeter = 2*(self.length + self.breadth)

# Rectangle1= Rectangle(5,6)
# Rectangle1.calculate_area()
# print("Area = ",Rectangle1.area)
# Rectangle1.calculate_perimeter()
# print("Perimeter = " , Rectangle1.perimeter)

# height = [1,8,6,2,5,4,8,3,7]
# max_area = 0
# for idx, vertical_line in enumerate(height):
#     for next_line_idx,next_line in height(height[idx + 1] ):
#         length =
#         breadth =
#         area = length * breadth
#         max_area = max(area,max_area)

# print(f"Maximum area of water: ", {max_area})

height = [1,8,6,2,5,4,8,3,7]
max_area = 0

for idx, vertical_line in enumerate(height):
    for next_idx in range(idx + 1, len(height)):
        
        length = min(vertical_line, height[next_idx])
        breadth = next_idx - idx
      
        area = length * breadth
        
        max_area = max(max_area, area)

print(f"Maximum area of water: {max_area}")

    



