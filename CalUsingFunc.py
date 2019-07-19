# There is an another way that is defining a function.
#-----------------------------------------------------
def switch_demo(op,a,b):
    switcher = {
        '+': int(a)+int(b),
        '-': int(a)-int(b),
        '*': int(a)*int(b),
        '/': int(a)/int(b)
    }
    if(op in switcher):
        print(a,op,b,"=",switcher[op])
    else:
        print("Unidentified Operation")
a = int(input("Enter first number"))
b = int(input("Enter second number"))
op = input("Enter opertion from below\n+\n-\n*\n/\n-------------------------\n")
switch_demo(op,a,b)