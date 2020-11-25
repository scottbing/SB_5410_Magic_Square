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

# create reversed array
r = b[:]
print("r = ", r)
# r[0].reverse()
# r[1].reverse()
# r[2].reverse()
# r[3].reverse()
# #reversed = list(map(lambda x: r, reverse))
# #r.reverse()
# print("r = ", r)

r = [i[::-1] for i in r[::-1]]
#print([i[::-1] for i in r[::-1]])
print("r = ", r)

# No print arrays
for x in b:
    print(*b, sep='')


from pandas import *
x = [["A", "B"], ["C", "D"]]
#df_no_indices = DataFrame.to_string(index=False)
#print(DataFrame.reset_index(drop=True, inplace=True))
#print(DataFrame.reset_index(drop=True))
print("\nTop Left")
forward = DataFrame(b)
print(forward.to_string(header=None, index=False))
print("\nBottom Right")
reverse = DataFrame(r)
print(reverse.to_string(header=None, index=False))
print(DataFrame(r))