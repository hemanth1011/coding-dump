a = int(input())
b = int(input())
c = int(input())
if(a>b):
    if(a>c):
        if(b>c):
            print(b,"is Second Biggest")
        else:
            print(c,"is Second Biggest")
if(b>c):
    if(a>c):
        print(a,"is Second Biggest")
    else:
        print(c,"is Second Biggest")
else:
    if(a>b):
        print(a,"is Second Biggest")
    else:
        print(b,"is Second Biggest")
