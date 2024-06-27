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

    @classmethod
        #This method is used to create object
    def create_object(cls,title, author_name, price, discount_rate):
        print("Inside classmethod: ",cls.class_variable)
        return cls(title, author_name, price, discount_rate)

    #Behaviour or methods section
    def calculate_sp(self):
        self.sp= self.price - (self.price * self.discount / 100 )
        # return sp

#calling class method
book1 = Book.create_object("Python", "Ross", 700, 10)
print(book1.title)