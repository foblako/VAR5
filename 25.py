def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    try:
        return sorted(d)[-1] - sorted(d)[0]
    except: return 0


for i in range(860000, 10**10):
    if div(i) % 100 == 18:
        print(i, div(i))

# 860040 430018
# 860163 286718
# 860219 27718
# 860240 430118
# 860440 430218
