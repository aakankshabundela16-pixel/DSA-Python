#natural number 1,2,3,4,5....n

def natural(n):
  if n==1:
    return 1
  
  elif n==0:
    return 0

  else:
    return natural(n-1) + n


print(natural(5))