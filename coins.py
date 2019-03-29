import math

def testPrime(n):
    if n==1 or n==2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range (3, maxdivisor+1,2):
        if n%i ==0:
            return False
    return True

def main():
    n = int(input('Enter a number:'))
    print(testPrime(n))
main()
    