def square_root(x):
    if x < 0:
        raise Exception("Trying to compute square root of negative number")
    return x**0.5


if __name__=="__main__":

    try:
        num = -10
        square_root_of_num = square_root(num)
        print("Square root: ", square_root_of_num)

    except Exception as e:
        print("Exception: ", e)
        # print("An error occurred, trying to compute square root of negative number")

