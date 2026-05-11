
def fib(n):
     if(n == 0 or n ==1):
         return(n)
     else:         return(fib(n-1) + fib(n-2))
 
recursion = fib(8)
print(recursion)


#def factorial(n):
  #  if n ==1:
     #   return 1
   # else:
    #    return n * factorial(n-1)
    
#print(factorial(5))


