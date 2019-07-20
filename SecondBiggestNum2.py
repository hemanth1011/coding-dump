a,b,c=[int(x) for x in input("Enter Elements with spaces").split(" ")]
if(a>b and a>c):
        a=0
else:
    if(b>c):
        b=0
    else:
        c=0
if(a>b and a>c):
        print(a,"is Second Biggest")
else:
    if(b>c):
        print(b,"is Second Biggest")
    else:
        print(c,"is Second Biggest")
