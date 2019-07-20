n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
     ele = int(input("Enter array element:"))
     arr.append(ele)
key = int(input("Enter Key element:"))
for i in arr:
    if(i>key**2):
        print(i)