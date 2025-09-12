a=(1,2,3)
b=(4,5,6)
lent=len(a)
mylis=[]
for item in range(lent):
    mylis.append(a[item]+b[item])
mytup=tuple(mylis)
print(mylis)


