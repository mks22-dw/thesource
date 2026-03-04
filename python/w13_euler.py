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

print('problem 1')
print('10: ', prob1(10))
print('1000: ', prob1(1000))

def prob6(limit):
    sum_squares = 0
    square_sum = 0
    n = 1
    while n <= limit:
        sum_squares+= n**2
        square_sum+= n
        n+= 1
    square_sum = square_sum**2
    return square_sum - sum_squares

print('\nproblem 6')
print('10: ', prob6(10))
print('100: ', prob6(100))


def prob5(n):
    guess = n
    max_divisor = 2
    while max_divisor <= n:
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            max_divisor = 2
            guess+= 1
    return guess

print('\nproblem 5')
print('10: ', prob5(10) )
print('20: ', prob5(20) )
