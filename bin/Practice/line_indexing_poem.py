f=open("Poem.txt","r")
g=open("PoemIndex","w")
st=f.readlines()
line=1
for i in st:
    index=0
    k=i.split()
    for j in k:
        g.writelines([j, ",line number:", str(line), ";", "index:", str(index), "\n"]) 
        index+=1
    line+=1
g.close()
f.close()
