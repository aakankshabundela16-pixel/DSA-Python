# a factorial is the product of every positive integer and all the positive is less then it

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))
