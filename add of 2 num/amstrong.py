n=int(input())
a=n
#r=0
sum=0
 #a=len(str(n))
while n>0:
       r=n%10
       sum=sum+r*r*r
       n//=10

if a==sum:
         print("is a amstrong number")
else:
        print("is not a amstrong")


