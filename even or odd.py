
'''
#using while loop
while True:
    n=int(input('enter no'))
    if n%2==0:
        print(n , "is even no")
    else:
        print(n ,"is odd no")

'''
from telnetlib import PRAGMA_HEARTBEAT


n=int(input('no'))
for i in range(1,n):
    if n%2==0:
        print(n,"is even no")
        if n%5==0:
            print(n,"is divided by 5")
            if n+5==20:
                break
    else:
        print('wrong no')
