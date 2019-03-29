import math
import time

### SOLVING PRIME COINS CHANGE USING DYNAMIC PROGRAMMING
def testPrime(n):
    if n==1 or n==2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range (3, maxdivisor+1,2):
        if n%i ==0:
            return False
    return True
def findCombi(amount, coins):
    combi =  [0]*(amount+1)
    combi[0] = 1

    for c in coins:
        for a in range(1,len(combi)):
            if a>= c:
                combi[a] += combi[a-c]
    
    return combi[amount]

def generatePrimeList(n):
    primeList = [1,2]
    for i in range(3,n+1,2):
        if testPrime(i):
            primeList.append(i)
    return primeList

def main():
    n = int(input('Enter a number:'))
    coins = generatePrimeList(n)
    result = findCombi(n,coins)
    print('Result is '+str(result))


main()
    