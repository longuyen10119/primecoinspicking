cdef int findCombiIterative(int amount, int coins, int sr, int lr):
    # generate a queue with tuples
    # (amount, index of coins, number of levels)
    
    queue = []
    # initial state
    # original amount, start w first coin, 0 level
    queue.append([amount,0,0])
    cdef int result = 0
    while len(queue)!=0:
        current = queue.pop(0)
        cdef int cAmount, cIndex, cLevel
        cAmount, cIndex, cLevel = current
        # Generate the next states
        cdef int i = 0
        for i in range(cIndex,len(coins)):
            cdef int nAmount, nLevel
            nAmount = cAmount - coins[i]
            nLevel = cLevel + 1
            if nAmount>0 and nLevel<lr:
                queue.append([nAmount,i,nLevel])
            if nAmount==0 and nLevel>=sr:
                result+=1
    return result

def generatePrimeList(n):
    primeList = [1, 2]
    for i in range(3, n, 2):
        if testPrime(i):
            primeList.append(i)
    primeList.append(n)
    return primeList


cdef bool testPrime(int n):
    if n == 1 or n == 2:
        return False
    maxdivisor = math.floor(math.sqrt(n))

    for i in range(3, maxdivisor+1, 2):
        if n % i == 0:
            return False
    return True