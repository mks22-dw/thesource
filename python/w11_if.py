def distance(x0, y0, x1, y1):
    d = (x1 - x0)**2 + (y1 - y0)**2
    d = d**0.5
    return d

def max3(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print("max3 tests")
b = max3(1, 2, 3)
print("3: ", b)
b = max3(1, 3, 2)
print("3: ", b)
b = max3(3, 2, 1)
print("3: ", b)

def closer_point(x0, y0, x1, y1, xtarget, ytarget):
    d0 = distance(x0, y0, xtarget, ytarget)
    d1 = distance(x1, y1, xtarget, ytarget)

    if d0 < d1:
        print("(", x0, ",", y0, ") is closer to (", xtarget, ",", ytarget, ")")
    elif d1 < d0:
        print("(", x1, ",", y1, ") is closer to (", xtarget, ",", ytarget, ")")
    else:
        print("the points are the same distance")

print("\ncloser_point tests")
xt = 5
yt = 10
x0 = -3
y0 = 4
x1 = 7
y1 = 8
closer_point(x0, y0, x1, y1, xt, yt)
closer_point(x1, y1, x0, y0, xt, yt)
closer_point(x0, y0, x0, y0, xt, yt)


def is_leap_year(year):
    if year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 100 == 0:
        print(year, "is not a leap year.")
    elif year % 4 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

print("\nis_leap_year_tests")
is_leap_year(2024)
is_leap_year(1900)
is_leap_year(2000)
is_leap_year(1983)
