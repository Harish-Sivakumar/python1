n=input()
c=n.split(" ")
a=c[0]
b=c[1]
for i in range(int(a),int(b)):
    if(i>1):
      if(i%2==0):
        continue
      else:
        print(i,end=" ")
    else:
        print("invalid one")