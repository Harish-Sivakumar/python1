n=input()
x=n.split(" ")
y=x[0]
z=x[1]
a=n
sum=0

 #a=len(str(n))
for n in range(int(y),int(z)):
   while n>0:
       r=n%10
       sum=sum*+r*r*r
       n//=10

if a==sum:
    print(a,"is a amstrong number")
else:
    print("is not a amstrong")