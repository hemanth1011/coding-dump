# Note : there is no switch case in python. so, here im using if and if-else statements.
#---------------------------------------------------------------------------------------
a = input("Enter first number")
b = input("Enter second number")
op = input("Enter opertion from below \n+\n-\n*\n/\n")
if(op=="+"):
    Result=float(a)+float(b)
if(op=="-"):
    Result=float(a)-float(b)
if(op=="*"):
    Result=float(a)*float(b)
if(op=="/"):
    Result=float(a)/float(b)
if(op=="+" or op=="-" or op=="*" or op=="/"):
    print("Result:",a,"+",b,"=",Result)
else:
    print("Unidentified Operation...")