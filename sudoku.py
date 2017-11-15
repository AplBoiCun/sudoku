# -*- coding: utf-8 -*-
def create_base():
    base = [[[1]*9 for c in range(9)] for r in range(9)]
    return base

def init_base1(base): #make nine dummies for 9x9 each cell
   a = list(map(int,input().split()))
   for r in range(9):
       for c in range(9):
           if a[r*9+c] != 0:
               base[r][c] = [0]*9
               base[r][c][a[r*9+c]-1]=1

def printer(base):
   print("\n  1 2 3 4 5 6 7 8 9")
   for r in range(9):
       bet=["A","B","C","D","E","F","G","H","I"]
       print(bet[r], end = '')
       for c in range(9):
           if base[r][c].count(1) != 1: #If there are more than one possiblity, it'll put dot
                   s = "."
           else:
               s = str(base[r][c].index(1)+1)
           print(' ' + s, end = '')
       print()
   print()

def eliminate(base,r,c):
    d = base[r][c].index(1)
    for x in range(9):
        base[r][x][d] = 0
    for x in range(9):
        base[x][c][d] = 0
    for x in range((r//3)*3,(r//3+1)*3):
        for y in range((c//3)*3,(c//3+1)*3):
            base[x][y][d] = 0
    base[r][c][d] = 1

def find(base):
    counter = 81
    for r in range(9):
        for c in range(9):
            if base[r][c].count(1) == 1:
                counter -= 1
                eliminate(base,r,c)
    return[base,counter]

def calc(base):
    while find(base)[1] !=0:
        base = find(base)[0]
        printer(base)
        calc(base)

def main():
    base = create_base()
    init_base1(base)
    printer(base)
    calc(base)

if __name__ == "__main__":
    main()


"""
    digits=["123456789"]
    rows=["ABCDEFGHI"]
    cols = digits
    squares =  cross(rows, cols)
    unitlist = ([cross(rows,c) for c in cols] +
                [cross(r,cols) for r in rows] +
                [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123', '456', '789')])
    units = dict((s,[u for u in unitlist if s in u]))
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)
"""

#input()
"""
4 0 0 0 0 0 0 0 0 0 0 0 7 0 0 2 9 0 0 8 0 0 3 6 0 0 0 0 0 7 0 0 0 0 0 8 0 0 3 0 0 2 0 0 0 1 0 0 0 0 0 0 5 0 0 6 0 0 0 8 0 0 0 0 0 2 9 0 0 7 3 0 0 0 0 0 1 0 0 0 4
0 0 5 0 0 0 6 0 0 0 6 0 3 0 0 0 0 8 7 1 0 6 0 0 0 9 0 0 0 3 2 1 8 7 4 6 0 7 0 4 3 9 5 8 2 0 0 0 0 0 0 9 0 1 4 8 9 1 0 0 0 7 5 2 3 1 7 9 5 8 6 4 0 5 0 0 2 4 3 0 0
4 0 0 0 0 0 0 0 0
0 0 0 7 0 0 2 9 0
0 8 0 0 3 6 0 0 0
0 0 7 0 0 0 0 0 8
0 0 3 0 0 2 0 0 0
1 0 0 0 0 0 0 5 0
0 6 0 0 0 8 0 0 0
0 0 2 9 0 0 7 3 0
0 0 0 0 1 0 0 0 4
"""
