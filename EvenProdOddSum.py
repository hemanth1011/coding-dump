num = input()
even = 1
odd = 0
l = len(num)
for i in range(0,l,2):
    even *= int(num[i])
for j in range(1,l,2):
    odd += int(num[j])
if(even % odd == 0):
    print(True)
else:
    print(False)