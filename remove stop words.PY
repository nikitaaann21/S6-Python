#remove stop words
# swords=["is","was","a","the","as"]
# s=input()
# words=s.split(" ")
# ns=""
# for w in words:
#     if w not in swords:
#         ns=ns+w+" "
# print(ns)

L=[]
n=int(input("Enter n"))
print("Enter elements")
for j in range(n):
    x=int(input())
    L.append(x)
print(L)

s=set()
n1=int(input("Enter n"))
print("Enter elements")
for i in range(n1):
    x1=int(input())
    s.add(x1)
print(s)