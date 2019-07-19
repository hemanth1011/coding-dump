import sys
argumentList = sys.argv
a = sys.argv[1]
op = sys.argv[2]
b = sys.argv[3]
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
    
# Note : Run via cmd prompt by open file location & type "cmd" in path area and enter "python filename.py args(with spaces)"
# For example: python arthcmd 10 + 20