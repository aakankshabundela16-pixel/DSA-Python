from array import*

arr = array('i', [])

n = int(input("enter your number"))

for i in range(0,n):
   arr.append(int(input("enter next number")))

for x in arr:
    print(x, end=',')

print('\n')

app = arr.index(1)
print(app)






