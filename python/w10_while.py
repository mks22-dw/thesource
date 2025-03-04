def fizz_buzz(limit):
    n = 1
    while n <= limit:
        if n % 15 == 0:
            print(n, "fizzbuzz!")
        elif n % 3 == 0:
            print(n, "fizz")
        elif n % 5 == 0:
            print(n, "buzz")
        n+= 1

print("fizz_buzz(20)")
fizz_buzz(20)


def fizz_what(limit, fizz_num, buzz_num):
    n = 1
    while n <= limit:
        if n % fizz_num == 0 and n % buzz_num == 0:
            print(n, "fizzbuzz!")
        elif n % fizz_num == 0:
            print(n, "fizz")
        elif n % buzz_num == 0:
            print(n, "buzz")
        n+= 1


print("\nfizz_what(50, 6, 9)")
fizz_what(50, 6, 9)


def sum_digs(n):
    s = 0
    while n > 0:
        s+= n % 10
        n = n // 10
    return s

print("\nsum_digs test")
print("sum_digs(87243):", sum_digs(87243))
