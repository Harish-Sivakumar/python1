a=input()
b=a.split(" ")
c=b[0]
d=b[1]
for i in range(int(c)+1,int(d)):
   # if i>1:

       for j in range(2,i):
           if(i%j)==0:
            break
       else:
            print(i)
