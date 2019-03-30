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
def findCombiDP(amount, coins, choice):
    combi =  [0]*(amount+1)
    combi[0] = 1

    for c in coins:
        for a in range(1,len(combi)):
            if a>= c:
                combi[a] += combi[a-c]
                choice.append(c)
        print (combi)
    
    return combi[amount]

def findCombiR(amount,coins, index,ls):
    if amount==0:
        ls.append('-')
        return 1
    if amount<0:
        return 0
    num = 0
    for coin in range(index,len(coins)):
        ls.append(coins[index])
        num += findCombiR(amount-coins[coin],coins,coin,ls)
    return num

def generatePrimeList(n):
    primeList = [1,2]
    for i in range(3,n+1,2):
        if testPrime(i):
            primeList.append(i)
    return primeList

def main():
    n = int(input('Enter a number: '))
    coins = generatePrimeList(n)

    # SOLVING with Recursive
    # ls = []
    # result = findCombiR(n,coins,0,ls)
    # print(ls)
    # print('---------------------')
    # print('Answer is ' + str(result))

    # Solving with DP 
    print(coins)
    print()
    choice = []
    result= findCombiDP(n,coins,choice)
    print('Answer is ' + str(result))
main()
    