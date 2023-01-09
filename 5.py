for n in range(100, 1000):
    r1 = int(str(n)[0]) ** 2 + int(str(n)[1]) ** 2
    r2 = int(str(n)[1]) ** 2 + int(str(n)[2]) ** 2
    r = str(r1) + str(r2)
    if r == "9752":
        print(n, r1, r2, r)

# 946
