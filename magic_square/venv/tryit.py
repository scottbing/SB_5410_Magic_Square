# include <stdio.h>
def main():
    n = 8
    # int row, col, num;
    for i in range(n):
        j = i
        for j in range(j,j+n):
            print(j + 1, end="")
            #n += 1
        print("")
    return 0


if __name__ == "__main__":
    main()
