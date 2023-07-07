#!/usr/bin/python3
import sys


def solutionQueen(n):
    col = set()
    posdiag = set()
    negdiag = set()
    board = [["_"] * n for i in range(n)]

    def getposition(board):
        pos = []
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == "Q":
                    pos.append([i, j])
        print(pos)

    def back(row):
        if row == n:
            getposition(board)
        for cl in range(n):
            if cl in col or row + cl in posdiag or row - cl in negdiag:
                continue
            board[row][cl] = "Q"
            col.add(cl)
            posdiag.add(row + cl)
            negdiag.add(row - cl)
            back(row + 1)
            board[row][cl] = "_"
            col.remove(cl)
            posdiag.remove(row + cl)
            negdiag.remove(row - cl)

    back(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutionQueen(n)
