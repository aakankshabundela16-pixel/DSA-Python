from numpy import*

val = array([1,2,3,4])

for x in val:
    print(x, end=',')

print('\n')

abc = array([1,2,4], float)

for y in abc:
    print(y, end=',')

print('\n')


cal = linspace(10, 20, 2)  #(startpoint, endpoint, kiatane equal parts karane he)

for k in cal:
    print(k, end=',')

print('\n')


non = arange(10 , 20 , 10) #(startno., endno., kitane ka difference rahega numbers ke bich)

for v in non:
    print(v, end=',')

sdd = logspace(10, 20, 3)

for j in sdd:
    print(j, end='')

print('\n')

same = zeros(5)    # zeros() ,zero print karata he

for c in same:
  print(c, end=',')

agg = ones(8)   #ones(), one print karata he 

for i in agg:
    print(i, end=',')

print('\n')


ram = full(10,4)  #full(kitane print karavane he, kya print karana he)

for h in ram:
    print(h, end=',')