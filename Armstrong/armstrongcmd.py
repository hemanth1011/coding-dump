# Using Command Line Arguments & No remainder operation

import sys
n = sys.argv[1]
sum = 0
for i in range(len(n)):
    sum += int(n[i])**len(n)
if(sum == int(n)):
    print(n,"is armstrong number")
else:
    print(n,"is not an armstrong number")
