
import time
import pyximport; pyximport.install()
import coinC

def main():
    st = input('Enter a number: ')
    arr = st.split(' ')
    arr = list(map(lambda x: int(x), arr))
    coins = coinC.generatePrimeList(arr[0])

#     SOLVING with Recursive
    start = time.time()
    result = coinC.findCombiIterative(arr[0],coins,arr[1],arr[2])
    print(result)
    print(time.time()-start)

main()