f=open('NOTES.txt','r')
a=f.read()
b=a.split()
c=0
for i in b:
    if i=='to':
        c+=1

print(b)
print(c)
f.close()
