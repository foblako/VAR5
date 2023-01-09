from itertools import *
k = 0
for i in product("AMOT", repeat=4):
    k += 1
    if "".join(i)[0] == "O":
        print(i, k)
        break

# 129
