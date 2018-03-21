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
    counter=len(w)
    print(counter)
    total = []
    for i in range(0, counter) :
        if w[i].isdigit() and i != counter-1 :
            var += w[i]
        elif w[i] ==w[counter-1]:
            var += w[i]
            total.append(var)
        else:
            total.append(var)
            var = ""
    print (total)
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
