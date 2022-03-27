import pickle

#10i
def CreateFile():
    a=int(input('enter book no:'))
    b=int(input('enter book name:'))
    c=int(input('enter Author name:'))
    d=int(input('enter price:'))
    record=[a,b,c,d]
f=open('book.dat','wb')
pickle.dump(record,f)
f.close()

#10ii
def countrec(author):
    f=open('STUDENT.DAT','rb')
    rec=pickle.load(f)
    c=0
    for i in rec:
        if i[2]=author:
            c+=1
    print('No. of books by author:', c)
