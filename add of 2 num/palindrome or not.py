n=int(input())
result=0
sum=0
a=n
while n>0:
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(a==sum):
        print("palindrome")
else:
        print("not palindrome")
