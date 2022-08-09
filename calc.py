def simpleCalculator():
    try:
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter second number : "))
    except ValueError:
        raise ValueError("Please enter Valid Numbers")

    operation = input('''
    Please enter your math operator :
    * multiplication
    / division
    + addition
    - subtraction
    ** Exponent
    % Modulus
    ''')

    if operation == "+":
        result = number1 + number2
        operationOutput = "{} + {} = {}".format(number1, number2, result)
        print(operationOutput)

    elif operation == "-":
        result = number1 - number2
        operationOutput = "{} - {} = {}".format(number1, number2, result)
        print(operationOutput)

    elif operation == "*":
        result = number1 * number2
        operationOutput = "{} * {} = {}".format(number1, number2, result)
        print(operationOutput)

    elif operation == "/":
        result = number1 / number2
        operationOutput = "{} / {} = {}".format(number1, number2, result)
        print(operationOutput)

    elif operation == "**":
        result = number1 ** number2
        operationOutput = "{} ** {} = {}".format(number1, number2, result)
        print(operationOutput)
    
    elif operation == "%":
        result = number1 % number2
        operationOutput = "{} % {} = {}".format(number1, number2, result)
        print(operationOutput)

    else:
        print("You did not enter the correct value")

    again()


def again():
    continueQuestion = input("Do you want to run again ? ")
    if continueQuestion.upper() == "Y":
        simpleCalculator()
    elif continueQuestion.upper() == "N":
        print("You are logged out. Thank you for your cooperation")
    else:
        again()


simpleCalculator()
