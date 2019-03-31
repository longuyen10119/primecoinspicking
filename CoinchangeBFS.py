import math
import time



def findCombiR(amount, coins, index, numCoinsAllowed):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    num = 0
    for coin in range(index, len(coins)):
        num += findCombiR(amount-coins[coin], coins, coin)
    return num


def testPrime(n):
    if n == 1 or n == 2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range(3, maxdivisor+1, 2):
        if n % i == 0:
            return False
    return True

def findCombiIterative(amount, coins, r):
    # generate a queue with tuples
    # (amount, index of coins, number of levels)
    
    queue = []
    # initial state
    # original amount, start w first coin, 0 level
    queue.append([amount,0,0])
    result = 0
    while len(queue)!=0:
        current = queue.pop(0)
        cAmount, cIndex, cLevel = current
        # Generate the next states
        for i in range(cIndex,len(coins)):
            nAmount = cAmount - coins[i]
            nLevel = cLevel + 1
            if nAmount>0 and nLevel<r[1]:
                queue.append([nAmount,i,nLevel])
            if nAmount==0 and nLevel>=r[0]:
                result+=1
    return result

def generatePrimeList(n):
    primeList = [1, 2]
    for i in range(3, n, 2):
        if testPrime(i):
            primeList.append(i)
    primeList.append(n)
    return primeList


def main():
    st = input('Enter a number: ')
    arr = st.split(' ')
    arr = list(map(lambda x: int(x), arr))

    coins = generatePrimeList(arr[0])

#     SOLVING with Recursive
    start = time.time()
    result = findCombiIterative(arr[0],coins,[arr[1],arr[2]])
    print(result)
    print(time.time()-start)

main()
