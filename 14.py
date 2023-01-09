def c(x):
    r = ""
    while x > 0:
        r += str(x % 5)
        x //= 5
    return r[::-1]


x = 5 ** 2022 - 2 * 5 ** 1010 + 25 ** 850 + 2500
print(c(x).count("4"))

# 690
