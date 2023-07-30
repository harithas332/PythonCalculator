from functools import reduce

def addition(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersSum = sum(newList)
    return NumbersSum


def subtraction(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersSub = newList[0] - sum(newList[1:])
    return NumbersSub

def multiplication(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersMult = reduce(lambda x, y: x*y, newList)
    return NumbersMult

def division(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersDiv = reduce(lambda x, y: x/y, newList)
    return NumbersDiv

print("Please enter your choice\n" +
      "1 -> Addition\n" +
      "2 -> Subtraction\n" +
      "3 -> Multiplication\n" +
      "4 -> Division\n")

choice = int(input("Enter your choice: "))
if 1 <= choice <= 4:
    print("Please enter your values: ")
    inputList = input().split()
    #print(inputList)


    if choice == 1:
        varList = addition(inputList)
        print("The sum of your inputs is: ", varList)
    elif choice == 2:
        varList = subtraction(inputList)
        print("The difference of you inputs is: ", varList)
    elif choice == 3:
        varList = multiplication(inputList)
        print("The product of your inputs is: ", varList)
    elif choice == 4:
        varList = division(inputList)
        print("The quotient of your inputs is: ", varList)
else:
    not_valid = "{} is not a valid choice\n".format(choice)
    print(not_valid)