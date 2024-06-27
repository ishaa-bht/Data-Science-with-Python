
continuee = True

while continuee is True :

        num1 = input("Enter first number ")
        num2 = input("Enter second number ")

                     



        calculate  = input ("Choose the type of calculation: \n 1. Arithmetic \n 2. Boolean ")

        if calculate == '1':

                num1 = int(num1)
                num2 = int(num2)

                print("Choose an operation to be performed: \n 1. Add ( + ) \n 2. Subtract ( - ) \n 3. Multiply ( * ) \n 4. Divide ( / ) \n 5. Modulus ( % ) \n 6. Exponential ( ^ ) \n 7. Floor Division ( // )    ")
                operation = input("Choose any one operation ")

                if operation == '1':
                        

                        sum = num1 + num2
                        print(f"{num1} + {num2} = {sum}")

                elif operation == '2':

                       

                        difference = num1 - num2
                        print(f"{num1} - {num2} = {difference}")

                elif operation == '3':
                        

                        product =  num1 * num2
                        print(f"{num1} * {num2} = {product}")

       
                elif operation == '4' :
                        
                        division =  num1 / num2
                        print(f"{num1} / {num2} = {division}")
        
                elif operation == '5' :
                        mod = num1 % num2
                        print(f"{num1} % {num2} = {mod}")

                elif operation == '6' :
                        exp = num1 ** num2
                        print(f"{num1} ^ {num2} = {exp}")

                elif operation == '7' :
                        fd = num1 // num2
                        print(f"{num1} // {num2} = {fd}")


                else :
                        print("Invalid input!")

        if calculate == '2':
                # num1 = bool(num1)
                # num2 = bool(num2)


                print("Choose an operation to be performed: \n 1. AND \n 2. OR  \n 3. NOT")
                operation = input("Choose any one operation ")

                if operation == '1' :
                        result_and = num1 and num2 
                        print(f"{num1} and {num2} = {result_and}")

                if operation == '2' :
                        result_or = num1 or num2 
                        print(f"{num1} or {num2} = {result_or}")

                if operation == '3' :
                        result_not1 = not num1 
                        result_not2 = not num2 
                        print(f"not {num1} = {result_not1} \nnot {num2} = {result_not2}")

                # if operation == '4' :
                #         result_xor = num1 ^ num2 
                #         print(f"{num1} xor {num2} = {result_xor}")

                     
        response = input('Continue? (y/n): ')

        if response == 'n':
                continuee = False


    


