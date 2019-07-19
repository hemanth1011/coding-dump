# Using input() & no remainder operation & using list 
n = input()
l = list(n)
print(l)
sum = 0
for i in range(len(l)):
    sum += int(l[i])**len(n)
if(sum == int(n)):
    print(n,"is armstrong number")
else:
    print(n,"is not an armstrong number")