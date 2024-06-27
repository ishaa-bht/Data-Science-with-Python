class Person:
    def __init__(self,name, age) :
        self._name = name
        self._age = age

#Getter methods
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
#Setter methods
    def set_name(self,name):
        self._name = name

    def set_age(self, age):
        self._age = age

person1 = Person("isha", 20)   

print (person1.get_name())
print(person1.get_age()) 

#updating values
person1.set_name("Nisha")
person1.set_age(21)
print (person1.get_name())
print(person1.get_age()) 

#==========================================================================
#.......Using property decoratpr for getter and setter methods.......

class Student:
    def __init__(self,name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        #Getter method for name
        print("Inside getter method for name")
        return self._name
    
    @property
    def age(self):
        #Getter method for age
        print("Inside getter method for age")
        return self._age
    
    @name.setter
    def name(self,name):
        #Setter method for name
        print("Inside setter method for name")
        self._name = name

    @age.setter
    def age(self,age):
        #Setter method for age
        print("Inside setter method for age")
        self._age = age

Student1 = Student("isha", 20)
print(Student1.name)
print(Student1.age)

Student1.name = "Jasmine"
Student1.age = 21
print(Student1.name)
print(Student1.age)

