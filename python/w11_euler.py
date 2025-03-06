def prob1(limit):
    total = 0
    n = 1
    while n < limit:
        if n % 3 == 0:
            total+= n
        elif n % 5 == 0:
            total+= n
        n+= 1
    return total

print("problem 1")
print("23:", prob1(10))
print("233168:", prob1(1000))

def sum_squares(limit):
    total = 0
    n = 1
    while  n <= limit:
        total+= n**2
        n+= 1
    return total
def square_sum(limit):
    total = 0
    n = 1
    while  n <= limit:
        total+= n
        n+= 1
    return total**2

def prob6(limit):
    return square_sum(limit) - sum_squares(limit)

print("\nproblem 6")
print("2640:", prob6(10))
print("25164150:", prob6(100))

def prob5(limit):
    #make an initial guess, start at limit since any
    #number must at least be divisible by limit
    guess = limit
    #all numbers are divisible by 1, so start
    #checking at 2
    divisor = 2
    while divisor <= limit:
        if guess % divisor != 0:
            guess+= limit
            divisor = 2
        else:
            divisor+= 1
    return guess

print("\nproblem 5")
#print("2520:", prob5(10))
#print("232792560:", prob5(20))


def euler_5(n):
    guess = n
    max_divisor = 1
    count = 0
    while max_divisor<= n:
        #count+= 1
        new_guess = guess
        while new_guess % max_divisor != 0:
            count+= 1
            new_guess+= guess
        guess = new_guess
        max_divisor+= 1
    #print("loop count: ", "{:,}".format(count))
    return guess
print("2520:", euler_5(10))
print("232792560:", euler_5(20))
