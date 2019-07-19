evensum=0
oddsum=0
evencount=0
oddcount=0
for i in range(1,101):
    if(i%2==0):
        evencount+=1
        evensum=evensum+i
    else:
        oddcount+=1
        oddsum=oddsum+i
print("Even Count=",evencount,"Even Sum=",evensum)
print("Odd Count=",oddcount,"Odd Sum",oddsum)