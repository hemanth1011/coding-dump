num = temp = int(input())
sum = 0
for i in range(len(str(num))):
    digit=temp%10
    sum=sum+digit
    temp=temp//10
print(sum)