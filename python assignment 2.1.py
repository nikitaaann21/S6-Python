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