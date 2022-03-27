f=open('NOTES.txt','r')
a=f.read()
b=a.split()
c=0
lower=[]
upper=[]
other=[]
for i in b:
    for j in i:
        if j.islower()==True:
            lower.append(j)
        elif j.isupper()==True:
            upper.append(j)
        else:
            other.append(j)
print('1:',lower, '2:',upper,'3:',other)
l=open('lower.txt','w')
l.writelines(lower)
u=open('upper.txt','w')
u.writelines(upper)
o=open('other.txt','w')
o.writelines(other)
f.close()
l.close()
u.close()
o.close()
