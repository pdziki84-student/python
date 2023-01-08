number_1 = float(input("Type first number: "))
number_2 = float(input("Type second number: "))

operation = input("Chosse operation: \n"
                  "1. Addition\n"
                  "2. Subtraction\n"
                  "3. Multiplication\n"
                  "4. Division\n")

if operation == "1":
   print("result: ", number_1 + number_2)
elif operation == "2":
    print("result: ", number_1 - number_2)
elif operation == "3":
    print("result: ", number_1 * number_2)
elif operation == "4":
    if number_2 == 0:
        print("Do not division by zero")
    else:
        print("result: ", number_1 / number_2)

            
