def calculator():
    '''
    This is our main function which entails the flow of our calculator program
    '''

    validMenuOptions = ["+", "-", "*", "/", "e"]
    while True:
        displayMenu()

        menuSelection = input("Enter your Option: ")

        # Handling user's menu input
        if menuSelection not in validMenuOptions:
            print("[-] Error: Invalid Input!")
        elif menuSelection == "e":
            print("[+] Program Terminated!")
            break
        else:
            # Asking user to enter numbers
            try:
                firstNumber = float(input("Enter 1st Number: "))
                secondNumber = float(input("Enter 2nd Number: "))

                result = 0

                # Checking each possibility and storing the output in 'result' variable
                if menuSelection == "+":
                    result = firstNumber + secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "-":
                    result = firstNumber - secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "*":
                    result = firstNumber * secondNumber
                    print("[+] Answer: ", result)
                elif menuSelection == "/":
                    if secondNumber == 0:
                        print("[-] Error: Cannot divide by zero")
                    else:
                        result = firstNumber / secondNumber
                        print("[+] Answer: ", result)
            except:
                print("[-] Error: Invalid Input! Only numerical input is allowed.")



def displayMenu():
    print("----------------------------")
    print("        Menu        ")
    print("Enter (+) for Addition")
    print("Enter (-) for Subtraction")
    print("Enter (*) for Multiplication")
    print("Enter (/) for Division")
    print("Enter (e) to Exit")
    print("----------------------------")


if __name__ == "__main__":
    calculator()