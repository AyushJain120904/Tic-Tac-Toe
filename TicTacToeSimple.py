import numpy as np
import sys
x = input('Enter choice for player 1(X=1 and O=0): ')
p,e = 0,0
if x == 'X' or x == 'x':
    p = 1
else:
    e = 1
print('Player 1 is:', p ,'     Player 2 is:', e)
a =np.full((3,3),-1)
for i in range(9):
    if i % 2 == 0:
        r,c = map(int,input("Enter row(1,2,3) and column(1,2,3) to put player 1 choice: ").split())
        while a[r-1][c-1] == e or a[r-1][c-1] == p:
            print('Position already acquired')
            r,c = map(int,input("Enter row and column to put player 1 choice: ").split())
        a[r-1][c-1] = p
    else:
        r,c = map(int,input("Enter row(1,2,3) and column(1,2,3) to put player 2 choice: ").split())
        while a[r-1][c-1] == p or a[r-1][c-1] == e:
            print('Position already acquired')
            r,c = map(int,input("Enter row and column to put player 2 choice: ").split())
        a[r-1][c-1] = e
    print(str(a).replace(' [', '').replace('[', '').replace(']', ''))
    for i in range(3):
          if a[i][1] == a[i][2] == a[i][0] == p or a[0][i] == a[1][i] == a[2][i] == p:
              print('Player 1 wins')
              sys.exit(0)
          elif a[i][1] == a[i][2] == a[i][0] == e or a[0][i] == a[1][i] == a[2][i] == e:
              print('Player 2 wins')
              sys.exit(0)
    if a[0][0] == a[1][1] == a[2][2] == p or a[0][2] == a[1][1] == a[2][0] == p:
        print('Player 1 wins')
        sys.exit(0)
    elif a[0][0] == a[1][1] == a[2][2] == e or a[0][2] == a[1][1] == a[2][0] == e:
        print('Player 2 wins')
        sys.exit(0)
else:
    print('It is a DRAW.')