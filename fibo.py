a=0
b=1

n=int(input("Enter the value of length"))
print(a,b)
while a+b<n:
    c=a+b
    print (c)
    a=b
    b=c
