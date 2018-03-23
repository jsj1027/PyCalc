import math


def main():
    func_list = userinput()
    total = inputparser(func_list)
    if total[1] == "+":
        addition(total[0], total[2])
    elif total[1] == "-":
        subtraction(total[0], total[2])
    elif total[1] == "*":
        multiplication(total[0], total[2])
    elif total[1] == "/":
        division(total[0], total[2])
    return None


def userinput():
    user_input = input("Function Entry, Format(Num Operator Num): ")
    func_list = list(user_input)
    return func_list

def inputparser(func_list):
    var = ""
    counter = len(func_list)
    total = []
    for i in range(0, counter):
        if func_list[i].isdigit() and i != counter - 1:
            var += func_list[i]
        elif not func_list[i].isdigit() and i != counter - 1:
            total.append(var)
            total.append(operation_check(func_list[i]))
            var = ""
        elif func_list[i].isdigit() and func_list[i] == func_list[counter - 1]:
            var += func_list[i]
            total.append(var)
    return total

def operation_check(op):
    if op in ["+", "-", "*", "/"]:
        return op
    else:
        exit("Error")


def addition(x, y):
    z = float(x) + float(y)
    print("The result is:", z)
    return None


def subtraction(x, y):
    z = float(x) - float(y)
    print("The result is:", z)
    return None


def multiplication(x, y):
    z = float(x) * float(y)
    print("The result is:", z)
    return None


def division(x, y):
    z = float(x) / float(y)
    print("The result is :", z)
    return None


main()
