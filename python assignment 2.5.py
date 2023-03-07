n = int(input("Enter the value of n: "))
s=str(n)
l=len(s)
sum=0
for i in range (l):
    x=s[i]
    d=int(x)
    sum+=d**l
if sum==n:
    print("Armstrong number")
else:
    print("Not Armstrong number")