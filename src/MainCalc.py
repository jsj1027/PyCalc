import math

def main(argv):
    """
    x = raw_input("First number: ")
    type(x)
    y = raw_input("Second number: ")
    type(y)
    division(x,y)
    """
    w = input("Function Entry, Format(Num Operator Num): ")
    w = list(w)
    var = ""
    operator = ""
    total = {}
    for temp in w:
        if temp.isdigit():
            var += str(temp)
        else:
            total.append(var)
    for temp in total:
        print(temp)
    return None

def operation_check(op):
    if op == "+":
        return True
    else :
        return False


def addition(x,y):
    z = x + y
    print("The added result equals:", z)
    return None

def subtraction(x,y):
    z = x - y
    print("The added result equals:", z)
    return None

def multiplication(x,y):
    z = x * y
    print("The added result equals:", z)
    return None

def division(x,y):
    z = float(x)/float(y)
    print("The added result equals:", z)
    return None

main("h")
