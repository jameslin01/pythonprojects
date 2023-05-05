#Factorial recursive function

def factorial(x):
    '''This is a recursive function to find the factorial of an integer
    '''
    
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num = 3

print("The factorial of",str(num), "is", factorial(num))

def fact(x):

    # Base case
    if x < 2: # i.e. if x = 0 or x = 1
        return 1
    # Recursive case
    else:
        return x * fact(x-1)

print(fact(3))