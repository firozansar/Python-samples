
def factorialIterative(x):
    total = 1
    while x>0:
        print("{0} * {1} ".format(total, x))
        total *= x       
        x-=1
    return total
  
print (factorialIterative(5))

print ("**** Recursive Factorial ********")

def factorialRecursive(n):
   if n < 1:   # base case
       return 1
   else:
       returnNumber = n * factorialRecursive(n - 1)  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

print (factorialRecursive(5))