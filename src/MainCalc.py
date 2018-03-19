import math

def main(argv):
    """
    x = raw_input("First number: ")
    type(x)
    y = raw_input("Second number: ")
    type(y)
    division(x,y)
    """
    w =  raw_input("Function Entry, Format(Num Operator Num): ")
    type(w)
    w = list(w)
    var = ""
    operator = ""
    total = []
    counter = 0
    total_count = len(w)
    for temp in w:
        while temp.isdigit():
            var += str(temp)
        else:
            total.append(var)
        while tem
    print total
    return None

def operation_check(op):
    if op : "+":
        return True

def addition(x,y):
    z = x + y
    print "The added result equals:", z
    return None

def subtraction(x,y):
    z = x - y
    print "The added result equals:", z
    return None

def multiplication(x,y):
    z = x * y
    print "The added result equals:", z
    return None

def division(x,y):
    z = float(x)/float(y)
    print "The added result equals:", z
    return None

main("h")
