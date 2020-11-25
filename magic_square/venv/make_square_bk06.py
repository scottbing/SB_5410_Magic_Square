from pandas import *        # use pandas DataFrame
import numpy as np

SIZE = 5
STOPAT = 8
TYPE='BR'

# build 'seed' array
a = [list(range(1, SIZE+1))]
#print(a)

if STOPAT < SIZE:
    for i in range(STOPAT, SIZE):
        a[0][i] = 0

#print("a after if:", a)

b = a[:]

# build forward array
for i in range(1, SIZE):
    b.append(list(range(i, SIZE+i)))
    #print("b", b)
    b[i].pop(0)
    #print("b", b)
    b[i].append(b[i][-1]+1)
    #print("b", b)

    STOPAT -= 1
    if STOPAT < SIZE:
        for j in range(STOPAT, SIZE):
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

if TYPE == 'TL':
    print("\nTop Left")
    forward = DataFrame(b)
    print(forward.to_string(header=False, index=False))

if TYPE == 'BR':
    print("\nBottom Right")
    reverse = DataFrame(r)
    print(reverse.to_string(header=False, index=False))

if TYPE == 'BL':
    print("\nBottom Left")
    reverseb = DataFrame(rb)
    print(reverseb.to_string(header=False, index=False))

if TYPE == 'TR':
    print("\nTop Right")
    reverser = DataFrame(rr)
    print(reverser.to_string(header=False, index=False))
