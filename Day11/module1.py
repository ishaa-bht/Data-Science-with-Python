import module2

def function():
    print("This is function of module")

print("__name__of module1: ",__name__)

if __name__ == "__main__":
    function()
    module2.function()