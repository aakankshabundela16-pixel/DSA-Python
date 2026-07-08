# imort array as arr

from array import*
val = array('i', [1,2,3,4,5,6,8,9]) #'i' int print

# val = array('d', [3.4,5.4,2,5]) #'d' float print
# val = array('u', ['a','d','s','e','f'])   #'u'character print

for i in range(0,len(val)):
   print(val[i], end=',')


print('\n')


for x in val:
    print(x, end=',')

print('\n')

print(val.typecode)

print(val.reverse())

for i in range(0,len(val)):
   print(val[i], end=',')

val.insert(1,78)
print(val)

val.append(100)
print(val)

val[2] = 300
print(val)

val.remove(4)
print(val)

abc = val[2 : 6] # if val[::-1] all el reverse
print(abc)

copyArray = array(val.typecode, (x for x in val))

copyArray.pop(3)

for i in range(0,len(copyArray)):
    print(copyArray[i] , end=" ")

