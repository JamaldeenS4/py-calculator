def addition(num_1, num_2):
    add = num_1 + num_2
    return add

def substraction(num_1, num_2):
    minus = num_1 - num_2
    return minus

def multiplication(num_1, num_2):
    divide = num_1 * num_2
    return divide

def division(num_1, num_2):
    divide = num_1 / num_2
    return divide


choice = ""
while True:
    
    print("1.ADD")
    print("2.MINUS")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.EXIT")
    choice = input("Enter Your Choice: ")
    
    if choice == "1" or choice == "ADD":
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        print("ANSWER: {}".format(addition(num_1, num_2)))
    elif choice == "2" or choice == "MINUS":
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        print("ANSWER: {}".format(substraction(num_1, num_2)))
    elif choice == "3" or choice == "MULTIPLY":
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        print("ANSWER: {}".format(multiplication(num_1, num_2)))
    elif choice == "4" or choice == "DIVIDE":
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        print("ANSWER: {}".format(division(num_1, num_2)))
    elif choice == "5" or choice == "EXIT":
        print("SEE YOU SOON!!")
        break
    else:
        print("Invalid Choice, Please try again.")
    