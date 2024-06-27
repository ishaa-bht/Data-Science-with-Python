from calculator import add, multiply

def area(length, breadth):
    return multiply(length, breadth)
def perimeter(length,breadth):
    return 2*add(length,breadth)

if __name__ == "__main__":
    print(area(10,20))
    print(perimeter(2,3))