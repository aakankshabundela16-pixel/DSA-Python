#fiboniacci series is a squence of number in which each number is the sum of the two privious number

def fab(n):
    if n==1 or n==2:  
        return 1

    else:
        return fab(n-1) + fab(n-2)

print(fab(6))

        