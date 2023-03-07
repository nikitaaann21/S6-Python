n = int(input("Enter the value of n: "))
s=str(n)
l=len(s)
sum=0
for i in range (l):
    x=s[i]
    d=int(x)
    fact=1
    for j in range(1,d+1):
        fact=fact*j
    sum+=fact
if sum==n:
    print("Krishnamoorthi number")
else:
    print("Not Krishnamoorthi number")
