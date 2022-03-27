f=open('poem.txt','r')
a=f.read()
b=a.split()
c=0
lst=['a','e','i','o','u','I']
for i in b:
    if i[0] in lst:
        c+=1
        
print(b)
print(c)
f.close()
