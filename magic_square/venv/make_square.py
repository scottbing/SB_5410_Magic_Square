from pandas import *  # use pandas DataFrame
import numpy as np

def make_square(size, stopat, type):
    # build 'seed' array
    a = [list(range(1, size + 1))]
    # print(a)

    if stopat < size:
        for i in range(stopat, size):
            a[0][i] = 0

    # print("a after if:", a)

    b = a[:]

    # build forward array
    for i in range(1, size):
        b.append(list(range(i, size + i)))
        # print("b", b)
        b[i].pop(0)
        # print("b", b)
        b[i].append(b[i][-1] + 1)
        # print("b", b)

        stopat -= 1
        if stopat < size:
            for j in range(stopat, size):
                b[i][j] = 0

    # print("rb:", list(reversed(b)))
    rb = list(reversed(b))

    # build reversed array
    r = b[:]
    # print("r = ", r)
    r = [i[::-1] for i in r[::-1]]
    # print("r = ", r)

    rr = list(reversed(r))

    # Print results
    pandas.set_option('display.max_colwidth', 4)

    if type == 'TL':
        print("\nTop Left")
        forward = DataFrame(b)
        print(forward.to_string(header=False, index=False))
        return forward.to_string(header=False, index=False)

    if type == 'BR':
        print("\nBottom Right")
        reverse = DataFrame(r)
        print(reverse.to_string(header=False, index=False))
        return reverse.to_string(header=False, index=False)

    if type == 'BL':
        print("\nBottom Left")
        reverseb = DataFrame(rb)
        print(reverseb.to_string(header=False, index=False))
        return reverseb.to_string(header=False, index=False)

    if type == 'TR':
        print("\nTop Right")
        reverser = DataFrame(rr)
        print(reverser.to_string(header=False, index=False))
        return reverser.to_string(header=False, index=False)


def main():
    size = 4
    stopat = 15
    type = 'BL'

    make_square(size, stopat, type)


if __name__ == "__main__":
    main()
