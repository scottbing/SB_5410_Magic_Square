from pandas import *        # use pandas DataFrame
import numpy as np

n=5
e=8
t='BR'

# build 'seed' array
a = [list(range(1, n+1))]
#print(a)

if e < n:
    for i in range(e, n):
        a[0][i] = 0

#print("a after if:", a)

b = a[:]

# build forward array
for i in range(1, n):
    b.append(list(range(i, n+i)))
    #print("b", b)
    b[i].pop(0)
    #print("b", b)
    b[i].append(b[i][-1]+1)
    #print("b", b)

    e -= 1
    if e < n:
        for j in range(e, n):
            b[i][j] = 0


#print("rb:", list(reversed(b)))
rb = list(reversed(b))


# build reversed array
r = b[:]
#print("r = ", r)
r = [i[::-1] for i in r[::-1]]
#print("r = ", r)

rr = list(reversed(r))

### Print results

if t == 'TL':
    print("\nTop Left")
    forward = DataFrame(b)
    print(forward.to_string(header=False, index=False))

if t == 'BR':
    print("\nBottom Right")
    reverse = DataFrame(r)
    print(reverse.to_string(header=False, index=False))

if t == 'BL':
    print("\nBottom Left")
    reverseb = DataFrame(rb)
    print(reverseb.to_string(header=False, index=False))

if t == 'TR':
    print("\nTop Right")
    reverser = DataFrame(rr)
    print(reverser.to_string(header=False, index=False))
