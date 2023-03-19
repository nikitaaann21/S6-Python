#remove stop words
swords=["is","was","a","the","as"]
s=input()
words=s.split(" ")
ns=""
for w in words:
    if w not in swords:
        ns=ns+w+" "
print(ns)
