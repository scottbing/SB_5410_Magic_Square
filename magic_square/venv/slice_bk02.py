n=4
a = []
b = []
r = []
a = [list(range(1, n+1))]
print(a)
b = a[:]
b.append(list(range(1, n+1)))
print("b", b)
b[1].pop(0)
print("b", b)
b[1].append(b[1][-1]+1)
print("b", b)
# print(a)
# print(a[1])
# print(a[1].pop(0))
# a[0].append(a[0][-1]+1)
# print(a)
b.append(list(range(2, n+2)))
print("b", b)
b[2].pop(0)
print("b", b)
b[2].append(b[2][-1]+1)
print("b", b)

b.append(list(range(3, n+3)))
print("b", b)
b[3].pop(0)
print("b", b)
b[3].append(b[3][-1]+1)
print("b", b)