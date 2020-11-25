n=4
a = []
b = []
r = []
a = [list(range(1, n+1))]
print(a)
b = a[:]

# build forward array
for i in range(1, n):
    b.append(list(range(i, n+i)))
    print("b", b)
    b[i].pop(0)
    print("b", b)
    b[i].append(b[i][-1]+1)
    print("b", b)

# b.append(list(range(2, n+2)))
# print("b", b)
# b[2].pop(0)
# print("b", b)
# b[2].append(b[2][-1]+1)
# print("b", b)
#
# b.append(list(range(3, n+3)))
# print("b", b)
# b[3].pop(0)
# print("b", b)
# b[3].append(b[3][-1]+1)
# print("b", b)

# create reversed array
r = b[:]
print("r = ", r)
r = [i[::-1] for i in r[::-1]]
print("r = ", r)

# No print arrays
for x in b:
    print(*b, sep='')


from pandas import *
x = [["A", "B"], ["C", "D"]]

print("\nTop Left")
forward = DataFrame(b)
print(forward.to_string(header=None, index=False))
print("\nBottom Right")
reverse = DataFrame(r)
print(reverse.to_string(header=None, index=False))
