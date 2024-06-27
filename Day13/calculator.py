
"""CALCULATOR

Returns:
    integer: _description_
"""
class Calculator:
    """
    MODULE TO PERFORM ARITHMETIC CALCULATION OF TWO OPERANDS
    """
    def __init__(self, num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2

    def __str__(self) -> str:
        return "THIS IS MY CALCULATOR CLASS"
    
    def add(self) -> int:
        """Adds two number

        Args:
            x (int): x is a integer
            y (int): _description_

        Returns:
            int: _description_
        """
        return self.num1 + self.num2
    def multiply(self) -> int:
        """Multiply two number

        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            int: _description_
        """
        return self.num1 * self.num2
    def div(self) -> int:
        """Divide two numbers

        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            int: _description_
        """
        return self.num1 / self.num2
    def sub(self) -> int:
        """Subtract two number

        Args:
            x (int): _description_
            y (int): _description_

        Returns:
            int: _description_
        """
        return self.num1 - self.num2   
if __name__ == "__main__":
    obj = Calculator(10, 20)
    print(obj.add())
    print(obj.multiply())
    print(obj.div())
    print(obj.sub())
    print(Calculator)
    print(obj)


