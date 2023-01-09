import math

a = [int(x) for x in open("17var05.txt")]

b = [a[i] + a[i - 1] for i in range(len(a) - 1) if
     a[i] > 0 and math.sqrt(a[i]).is_integer() or a[i - 1] > 0 and math.sqrt(a[i - 1]).is_integer()]
print(len(b), max(b))

# 60 18555
