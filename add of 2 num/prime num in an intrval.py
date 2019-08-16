start=int(input("enter 1st num"))
stop=int(input("enter 2nt num"))
for i in range(start,stop+1):
   # if i>1:

       for j in range(2,i):
           if(i%j)==0:
            break
       else:
            print(i)
