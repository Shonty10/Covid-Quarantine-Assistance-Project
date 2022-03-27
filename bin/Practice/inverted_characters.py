f=open("NOTES.txt",'r')
s=f.read()
f.close()

s1=s.swapcase()
f1=open('inverted.txt','w')
f1.writelines(s1)
f1.close()
