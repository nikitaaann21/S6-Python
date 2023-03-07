n=int(input("Enter no.: "))
l=[]
for i in range (n):
    x=int(input())
    l.append(x)
print("Min =",min(l))
print("Max =",max(l))
print("Avg =",sum(l)/len(l))
l.sort()
print(l)
l.sort(reverse=True)
print(l)
L=[i**2 for i in range(1,11)]
#range 1 to 11 for 10 numbers(not including 11 as<11)
print(l)
print(L)
#case sensitive
L1=[10,20,30]
L2=[1,2,3]
L3=zip(L1,L2)
for i in L3:
    print(i)
#here i will be each character in  string L3, not index value
