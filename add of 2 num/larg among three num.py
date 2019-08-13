n=(input())
a=n[0]
b=n[1]
c=n[2]
if(a>=b and a>=c):
    print(a)
elif(b>=c and b>=a):
        print(b)
else:
    print(c)