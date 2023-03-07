n=int(input("Enter no.: "))
s=str(n)
l=len(s)
a=""
for i in s:
    if i=="1":
        a+="One"
    elif i=="2":
        a+="Two"
    elif i=="3":
        a+="Three"
    elif i=="4":
        a+="Four"
    elif i=="5":
        a+="Five"
    elif i=="6":
        a+="Six"
    elif i=="7":
        a+="Seven"
    elif i=="8":
        a+="Eight"
    elif i=="9":
        a+="Nine"
    elif i=="0":
        a+="Zero"
    a+=" "
print(a)


