n = int(input("Enter the value of n: "))
s=str(n)
l=len(s)
r= s[::-1]
print("Reverse is",r)
print(r)
sum=0
for i in range (l):
    x=s[i]
    sum+=int(x)
print(sum)