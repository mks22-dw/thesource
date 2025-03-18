def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2 + (y1 - y0)**2
    d = d**0.5
    return d

print("distance tests:")
print("5.0: ", distance(3, 0, 0, 4))
print("1.0: ", distance(1, 0, 2, 0))
print("17.0:", distance(0, 0, 8, 15))

def f_to_c(ftemp):
    celsius = (ftemp - 32) * (5/9)
    return celsius

print("\nf_to_c tests:")
print("0.0: ", f_to_c(32.0))
print("100.0: ", f_to_c(212.0))
print("-40.0: ", f_to_c(-40))

def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c

print("\neval_quadratic tests:")
print("4: ", eval_quadratic(1, 0, 3, 1))
print("6: ", eval_quadratic(1, 2, 3, 1))
print("7: ", eval_quadratic(1, 0, 3, 2))


def is_even(n):
    return n % 2 == 0

print("\nis_even tests:")
print("True: ", is_even(12))
print("False: ", is_even(11))
print("True: ", is_even(0))
