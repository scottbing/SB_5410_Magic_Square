# include <stdio.h>
def make_seed(n):
    board = []
    for i in range(n):  # create a list with nested lists
        board.append([])
        for j in range(n):
            board[i].append("O")  # fills nested lists with data
    return board

def main():
    n = 4
    square = make_seed(n)
    print(square)
    # int row, col, num;
    for i in range(n):
        j = i
        for j in range(j,j+n):
            row = j + 1
            print(" ", row, " ", end="")
        print("")
    return 0


if __name__ == "__main__":
    main()


# z = list(range(1, n+1))
# print(z)