import math
def isPrime(a):
    x=False
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                x = True
                break
    return x

def largest_prime_fact(a):
    l=[]
    for i in range(2,int(math.sqrt(a))):
        if(a%i==0 and not isPrime(i)):
            l.append(i)
    return max(l)

print(largest_prime_fact(600851475143))