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

print("classic solution:")
start = time.time()
answer = euler5(10)
elapsed = time.time() - start
print("euler5(10): ", answer, elapsed)

start = time.time()
answer = euler5(20)
elapsed = time.time() - start
print("euler5(20): ", answer, elapsed)


def euler5_better(n):
    loops = 0
    guess = n
    max_divisor = 2
    while max_divisor <= n:
        loops+= 1
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= n
            max_divisor = 2
    print("# of loops:", loops)
    return guess

# print("\nbetter solution:")
# start = time.time()
# answer = euler5_better(10)
# elapsed = time.time() - start
# print("euler5(10): ", answer, elapsed)
#
# start = time.time()
# answer = euler5_better(20)
# elapsed = time.time() - start
# print("euler5(20): ", answer, elapsed)


loops = 0
#assume a < b
def lcm(a, b):
    global loops
    multiple = b
    while multiple % a != 0:
        loops+= 1
        multiple+= b
    return multiple

def euler5_lcm(n):
    guess = n
    max_divisor = 1
    while max_divisor<= n:
        guess = lcm(max_divisor, guess)
        max_divisor+= 1
    print("loops:", loops)
    return guess

# print("\nlcm solution:")
# start = time.time()
# answer = euler5_lcm(20)
# elapsed = time.time() - start
# print("euler5_lcm(20):", answer, elapsed)

# start = time.time()
# answer = euler5_lcm(20)
# elapsed = time.time() - start
# print("euler5_lcm(20):", answer, elapsed)
