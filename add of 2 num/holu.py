def hari(n):
    for i in range(0,n+1):
        for j in range(n, 0, -1):
           print("*" *(n-i))
            print(" " * (n - j) + "*" * j)


       # print(" " * (n - j) + "*" * j)
n = 5
hari(n)
'''
def ish(n):
       for j in range(n,0,-1):
           print(" " *(n-j) + "*" *j)
n=5
ish(n)
'''


