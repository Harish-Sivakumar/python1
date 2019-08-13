n=input("enter the character")
vowel=['a','e','i','o','u']

#if(n==chr):
if(n.isalpha()):

   if(n in vowel):
        print("it is vowel")
   else:
        print("not vowel")
elif(n!=n.isalpha()):
    print("invalid")
