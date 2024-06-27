class Person:
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print("I am displaying person info")
        print("Name: ", self.name)
        print("Age: ",self.age) 
        print("Address:",self.address)
    def person_method(self):
        print("I am a person and i can walk.")
class Student(Person):
    def __init__(self, name, age, address,university):
        super().__init__(name, age, address)
        self.university = university

    #Person class has same name display_info(), so this will override that method
    #To call the overrided method of person class, we need to use super()

    def display_info(self):
        super().display_info()
        print("University: ", self.university)

    def student_method(self):
        print("I am a student and i can study")



#Creating objects of subclass
Student1 = Student("isha", 19, "Biratnagar", "Tribhuvan University")
Student1.display_info()
Student1.person_method()
Student1.student_method()

#shape=class
#rect and corcle=subclass
#method area and perimeter

class Shape:
    def __init__(self,name):
        self.name = name

    def display_info(self):
        print("SHAPE : ", self.name)


class Rectangle(Shape):
    def __init__(self, name,length,breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        area = self.length * self. breadth
        return area
    def calc_peri(self):
        peri= 2*(self.length + self.breadth)
        return peri
    
class Circle(Shape):
    def __init__(self, name,radius):
        super().__init__(name)
        self.radius = radius
        

    def calc_area(self):
        area = (22/7)*self.radius**2
        return area
    def calc_peri(self):
        peri= 2*(22/7)*self.radius
        return peri
    
Rect = Rectangle("Rectangle",5,6)
print("Area:",Rect.calc_area())




        



    