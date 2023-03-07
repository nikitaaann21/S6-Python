#SET
s={10,20,30}
s2={20,30,40,50}
print("s:",s)
print("s2:",s2)
#slicing (like s[-1] or s[0]) is not possible
print("min:",min(s))
print(f'max:{max(s)}')
#prints variable in {} withut breaking string
print("union",s|s2)
print("difference",s-s2)
print("intersection",s&s2)
print("symmetric difference",s^s2)
print("s2 is subset of s?",s.issubset(s2))
#addition by s+s2 or scalar multiplication by s*2 not possible
s.add(90)
print(s)
n=int(input("Enter n"))
s4=set()
for i in range(n):
    x=int(input('item:'))
    s4.add(x)
print(s4)

