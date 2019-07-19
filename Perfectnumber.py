num = int(input())
sum = 0
for i in range(1,num):
    if (num % i) == 0:
        sum += i
if(num == sum):
    print(num,"is perfect number")
else:
    print(num,"is not a perfect number")