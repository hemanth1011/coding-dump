# Using List Comprehension & No remainder operation 
n = input()
lc = [int(n[i])**len(n) for i in range(len(n))] 
if(sum(lc)==int(n)):
    print(n,"is armstrong number")
else:
    print(n,"is not an armstrong number")