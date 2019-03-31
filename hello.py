import time
import pyximport; pyximport.install()
import simple
def main():
    start = time.time()
    result = simple.count(1000)
    duration = time.time() - start
    print(result, duration)
 
 
if __name__ == '__main__':
    main()