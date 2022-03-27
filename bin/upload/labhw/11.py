import pickle
def CountRec():
    f=open('STUDENT.DAT','rb')
    rec=pickle.load(f)
    c=0
    for i in rec:
        if int(i[2])>80:
            print(i[0],i[1],i[2])
        if int(i[2])>75:
            c+=1
    print('No. of students scoring above 75:', c)
            
