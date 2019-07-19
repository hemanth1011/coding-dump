num = temp = int(input())
rev = 0
for i in range(len(str(num))):
    digit=temp%10
    rev = rev*10+digit
    temp=temp//10
print(rev)