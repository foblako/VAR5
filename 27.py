f = open("27v05_A.txt")
n = int(f.readline())
m = [0] * 123
l = [0] * n
s = 0
ms = 10 ** 20
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 123 == 0: ms = min(ms, s)
    s1 = s - m[s % 123]

    m[s % 123] = max(m[s % 123], s1)
print(ms)
