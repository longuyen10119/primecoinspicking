import math
import time



def findCombiR(amount, coins, index, numCoins,lr,hr):
    if amount < 0:
        return 0
    if numCoins > hr:
        return 0
    if amount == 0 and numCoins>=lr:
        return 1
    if amount>0 and numCoins==hr:
        return 0
    num = 0
    for coin in range(index, len(coins)):
        if amount>=coins[coin]:
            num += findCombiR(amount-coins[coin], coins, coin,numCoins+1,lr,hr)
        else:
            break
    return num


def testPrime(n):
    if n == 1 or n == 2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range(3, maxdivisor+1, 2):
        if n % i == 0:
            return False
    return True


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

    start = time.time()
    num = arr[0]
    lr =0
    hr = 0
    if len(arr)==1:
        lr = 1
        hr = num
    elif len(arr)==2:
        lr = arr[1]
        hr = arr[1]
    else:
        lr = arr[1]
        hr = arr[2]

    result = findCombiR(arr[0],coins,0,0,lr,hr)

    print(result)
    print(time.time()-start)

main()
