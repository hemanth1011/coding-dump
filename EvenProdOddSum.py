num = input()
even = 1
odd = 0
l = len(num)
for i in range(0,l,2):
    if(i%2==0):
        even *= int(num[i])
    else:
        odd += int(num[i+1])
if(even % odd == 0):
    print(True)
else:
    print(False)