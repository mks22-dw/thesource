import time

def euler5(n):
    loops = 0
    guess = n
    max_divisor = 2
    while max_divisor <= n:
        loops+= 1
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 2
    print("# of loops:", loops)
    return guess

start = time.time()
answer = euler5(10)
elapsed = time.time() - start
print("euler5(10): ", answer, elapsed)

start = time.time()
answer = euler5(20)
elapsed = time.time() - start
print("euler5(20): ", answer, elapsed)
