from math import *
from random import random, randrange 


#def random_shuffle(x):
   # length = len(x)
    #for i in range(length-1,0,-1):
    #    x[i]=x[randrange(0,i)]
   # return x
    



#print(random_shuffle([3,4,5]))

def knuth_shuffle(x):
    for i in range(len(x)-1, 0, -1):
        j = randrange(i + 1)
        x[i],x[j]=x[j],x[i]
    return x
for i in range(100):
    print(knuth_shuffle([3,4,5]))

print(2)

