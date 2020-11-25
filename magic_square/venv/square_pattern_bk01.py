# include <stdio.h>
def main():
    n = 5
    # int row, col, num;
    for i in range(n):
        j = i
        #print("j = ", j)
        for j in range(j,j+n):
            print(j + 1, end="")
            #n += 1
        print("")
    return 0


if __name__ == "__main__":
    main()
