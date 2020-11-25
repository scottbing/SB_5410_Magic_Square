from pandas import *        # use pandas DataFrame

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


#print("rb:", list(reversed(b)))
rb = list(reversed(b))


# build reversed array
r = b[:]
print("r = ", r)
r = [i[::-1] for i in r[::-1]]
print("r = ", r)

rr = list(reversed(r))

### Print results

print("\nTop Left")
forward = DataFrame(b)
print(forward.to_string(header=False, index=False))
print("\nBottom Right")
reverse = DataFrame(r)
print(reverse.to_string(header=False, index=False))

print("\nBottom Left")
reverseb = DataFrame(rb)
print(reverseb.to_string(header=False, index=False))

print("\nTop Right")
reverser = DataFrame(rr)
print(reverser.to_string(header=False, index=False))
