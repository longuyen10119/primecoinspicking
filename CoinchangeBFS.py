import math
import time

# SOLVING PRIME COINS CHANGE USING DYNAMIC PROGRAMMING


def testPrime(n):
    if n == 1 or n == 2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range(3, maxdivisor+1, 2):
        if n % i == 0:
            return False
    return True

def findCombiIterative(amount, coins):
    # generate a queue with tuples
    # (amount, index of coins, number of levels)
    
    queue = []
    # initial state
    # original amount, start w first coin, 0 level
    queue.append([amount,0,0])
    result = []
    while len(queue)!=0:
        current = queue.pop(0)
        cAmount, cIndex, cLevel = current
        # Generate the next states
        for i in range(cIndex,len(coins)):
            nAmount = cAmount - coins[i]
            nLevel = cLevel + 1
            if nAmount>0:
                queue.append([nAmount,i,nLevel])
            if nAmount==0:
                result.append(nLevel)
    return result

def generatePrimeList(n):
    primeList = [1, 2]
    for i in range(3, n+1, 2):
        if testPrime(i):
            primeList.append(i)
    primeList.append(n)
    return primeList


def main():
    n = int(input('Enter a number: '))
    coins = generatePrimeList(n)

#     SOLVING with Recursive
    
    result = findCombiIterative(n,coins)
    print('---------------------')
    
    end = 0
    test = [i for i in range(5,11)]
    for r in result:
        if r in test:
            end+=1
    print(end)

main()
