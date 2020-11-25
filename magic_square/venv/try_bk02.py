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

# build reversed array
r = b[:]
print("r = ", r)
r = [i[::-1] for i in r[::-1]]
print("r = ", r)



from pandas import *
x = [["A", "B"], ["C", "D"]]

print("\nTop Left")
forward = DataFrame(b)
print(forward.to_string(header=None, index=False))
print("\nBottom Right")
reverse = DataFrame(r)
print(reverse.to_string(header=None, index=False))
