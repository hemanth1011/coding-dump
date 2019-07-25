n = int(input())
col = n
for i in range(1,n+1):
    print(' '*col,'*'*i,end=' ')
    col-=1
    print("\n")