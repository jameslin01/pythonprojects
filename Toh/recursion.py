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

def factorial(x):

    # Base case

    if x == 0:

        return 1
    
    if x == 1:
        return 1
    
    else:

        return(x * factorial(x-1))

def list_sum(num_List):
    # Base case
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

print(list_sum([1,2,3,4]))
    