l=[20,2.3,"mec"]
l1=[10,3+2j,[10,20]]
l2=["sreya","is","my","boo"]
print(l,l1,l2)
print("list l is ",l)
print("l[-1] is ",l[-1])
print("l[-2] is ",l[-2])
print("l[-3] is ",l[-3])
print("l[0] is ",l[0])
print("l[1] is ",l[1])
print("l[2] is ",l[2])

print("l[0:3]: ",l[0:3])#will print l[0],l[1],l[2]


print("len of l3",len(l))



#print("sum of l3",sum(l))
#print("min of l3",min(l))
#print("max of l3\n\n",max(l))

print(l)
print("reversed l3: ",l.reverse())
#print("sorted l3: ",l.sort())
#print("sort l3 in reverse order:",l.sort(reverse=True))#sort in reversed order

l=l+[20]
print("l3=l3+[20]",l)
#print("l3.append(300): ",l.append[300])
print("l3.extend([100,200]): ",l.extend([100,200]))
print("l3.insert(1,1000):",l.insert(1,1000))