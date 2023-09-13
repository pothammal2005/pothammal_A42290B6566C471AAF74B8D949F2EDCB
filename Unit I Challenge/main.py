def fact(n):
 """this the a recursive function 
to find the factorial of an integer"""
 if n == 0:
  return 1
 else:
  return(n * fact(n-1))
fact(5)
  