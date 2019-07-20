a = int(input())
b = int(input())
c = int(input())
if(a>b):
    if(a>c):
        if(b>c):
            print(b)
        else:
            print(c)
if(b>c):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(a>b):
        print(a)
    else:
        print(b)
        