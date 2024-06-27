#Program to generate square of odd numbers only
#if number is even raise exception

number = int(input("Enter a number: "))

class SquareOfOddError(Exception):
    def __init__(self, number, *args):
        self.number= number
        self.message = f"{number} is an even number"
        super().__init__(self.message)

        

if __name__ == "__main__":
    try:
        if number% 2 != 0:
            result = number**2
            print("Square of the odd number is: ", result)
        else:
            raise SquareOfOddError(number)
    except SquareOfOddError as e:
        print(e.message)
        print("Square of even number is not possible in our program")
    print("End of program")