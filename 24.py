s = open("24var05-08.txt").readline()
while "00" in s: s = s.replace("00", "*")
s = s.split("*")
s.sort(key=len)
print(s[-1])
print(len(s[-1]) + 2)

# 977
