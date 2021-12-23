
# default reference type function arguments act as 'static' variables
# and hold their values on successive function calls

def f(i, values = []):
    values.append(i)
    print (values),
    return values
f(1)
f(2)
f(3)

def f2(i, values = []):
    values.append(i)
    print (values)

f2(1)
f2(2)
f2(3)


