from math import *

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
def pow(a, b):
    return a ** b
def exp(a):
    return exp(a)
def log(a):
    return log(a)
def sum(a):
    return fsum(a)


request = input("Simple operation: ") # Reads string from the standard input

if "(" in request:
    tokens = request.replace(")","").split("(")
    tokens = tokens[:len(tokens)]
    print(tokens)

else:
    tokens = request.split(" ")
    print(tokens)

if len(tokens) == 1:
    print("Write in the form : ...")

elif len(tokens) == 3: # Binary operation
    a = float(tokens[0])
    b = tokens[1]
    c = float(tokens[2])
elif len(tokens) == 2: # Unary operation
    #a = tokens[0]
    #b = float(tokens[1])
    b = tokens[0]
    a = float(tokens[1])
else:
    b = tokens[0]
    a = []
    for t in tokens[1:]:
        a.append(float(t))
if b == '+':
    print(add(a, c))
elif b == '-':
    print(sub(a, c))
elif b == '*':
    print(mult(a, c))
elif b == '/':
    print(div(a, c))
elif b == '^':
    print(pow(a, c))
elif b == 'exp':
    print(exp(a))
elif b == 'log':
    print(log(a))
elif b == 'sum':
    print(sum(a))


