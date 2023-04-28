
ciphertext = 8 * [0]
e = 8 * [5]
N = 8 * [0]

data_packets = [ ((N[i],e[i]), ciphertext[i]) for i in range(8)]

print(data_packets)



def gcd(a,b):
    """Returns the greatest common divisor of integers a and b using Euclid's algorithm.
    The order of a and b does not matter and nor do the signs."""
    if not(a%1 ==0 and b%1==0):
        print( "Need to use integers for gcd.")
        return None
    if b==0:
        return abs(a)                           #Use abs to ensure this is positive
    else:
        return gcd(b,a%b)
    
print(gcd(16*7,37))

