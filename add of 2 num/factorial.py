# n=int(input("enter"))
def factorial(num):
    return 1 if (num==1 or num==0)  else num*factorial(num-1)

num=2
factorial(num)
print(factorial(num))
