
#1> stack

def isempty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        print("Underflow")
    else:
        print("deleted item:", stk.pop())
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1

def peek(stk):
    if isempty(stk):
        print("Empty stack")
    else:
        top=len(stk)-1
        print(stk[top],"<--top")

def display(stk):
    if isempty(stk):
        print("empty stack")
    else:
        top=len(stk)-1
        print(stk[top],"<--top")
        for i in range(top-1,-1,-1):
            print(i)

stack=[]
top=None
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    ch=int(input("Enter choice:"))
    if ch==1:
        item=int(input("Enter item:"))
        push(stack,item)
    elif ch==2:
        pop(stack)
    elif ch==3:
        peek(stack)
    elif ch==4:
        display(stack)
    elif ch==5:
        exit()
    else:
        print("invalid")
####
#2>

def accept():
    for i in range(10):
        item=int(input("enter numeric element for list:"))
        lst.append(item)
def bubble_sort(lst):
    l=len(lst)
    for i in range(l-1):
        for j in range(0,l-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
def display(lst):
    print("sorted list:",lst)

lst=[]
while True:
    print("1.Accept numbers")
    print("2.Bubble sort")
    print("3.Display")
    ch=int(input("enter choice:"))
    if ch==1:
        accept()
    elif ch==2:
        bubble_sort(lst)
    elif ch==3:
        display(lst)
    else:
        print("invalid")
####
#3>
f=open("NOTES.txt","w")
f.write("We all have been affected by the current Covid-19 pandemic. However, the impact of the pandemic and its consequences are felt differently depending on our status as individuals and as members of soceity. While some try to adapt to wokring online, homeschooling their children and ordering food via Instacart, others have no choice but to be exposed to the virus while keeping society functioning.")
f.close()
c_the=0
c_to=0
#f.close()
f=open("NOTES.txt", "r")
st=f.read()
k=st.split()
for i in k:
    if i.upper()=="THE":
        c_the+=1
    if i.upper()=="TO":
        c_to+=1
print("count of The/the:",c_the)
print("count of To/to:", c_to)

####
##4>
f=open("Poem.txt","w")
line="Whose woods these are i think i know\nHis house is in the village though;\nHe will not see me stopping here\nTo watch his woods fill up with snow"
f.write(line)
f.close()
f=open("Poem.txt","r")
st=f.read()
k=st.split()
c=0
for i in k:
    if i[0].upper() in ['A','E','I','O','U'] and i[len(i)-1].upper() in ['A','E','I','O','U']:
        c+=1
print("count of words starting and ending with vowel:",c)

###5>
f=open("TEXT.txt","w")
g=open("up.txt","w")
h=open("low.txt","w")
j=open("oth.txt","w")
line=input("enter text:")
f.write(line)
f.close()
f=open("TEXT.txt","r")
st=f.read()
k=st.split()
for i in k:
    if i.isupper()==True:
        g.write(i)
    elif i.islower()==True:
        h.write(i)
    else:
        j.write(i)
f.close()
g.close()

h.close()
j.close()

###6>
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

##7>

import csv
fields=['name','eng','math','phy','comp','chem']
rows=[]
name=input("enter name:")
marks_e=float(input("enter marks for eng:"))
marks_m=float(input("enter marks for math:"))
marks_p=float(input("enter marks for phy:"))
marks_co=float(input("enter marks for comp:"))
marks_ch=float(input("enter marks for chem:"))
totmarks=marks_e+marks_m+marks_p+marks_co+marks_ch
avgmarks=totmarks/5
rows.append([name,marks_e,marks_m,marks_p,marks_co,marks_ch,totmarks,avgmarks])
print(rows)
    
with open("studentmarks.csv","a") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
##8> as prg 5

###9>
f=open("Poem.txt","r")
e=open("invertpoem.txt","w")
st=f.read()
for i in st:
    if i.isupper():
        e.write(i.lower())
    if i.islower():
        e.write(i.upper())
f.close()
e.close()
        
