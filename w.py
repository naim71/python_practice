n = int(input("Insert a number: \n"))
i = 2
def isPrime(n,i):
  if(n==0 and n==1):
   return False

  if (n==i):
   return True

  if (n%1==0):
    return True

if(isPrime(n,i)==True):
  print("Given Number is a Prime number")
else: print("It's not a Prime number.")