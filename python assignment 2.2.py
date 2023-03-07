n= int(input("Enter n: "))
i=3
s=0
a="+"
s=" x"
while i<=n:
    if a =="+":
       a="-"
    else:
       a="+"

    s=s+a+"x^"+str(i)+"/"+str(i)+"!"
    i=i+2
print(s)
x= int(input("Enter x: "))
sum=x
flag=0
i=3
while i<=n:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    t=(x**i)/fact
    if flag ==0:
       sum-=t
       flag=1
    else:
       sum+=t
    i=i+2
print(sum)    