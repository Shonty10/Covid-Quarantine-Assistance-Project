def is_empty(l):
    if len(l)==0:
        return True
    else:
        return False
def push(l,e):
    l.append(e)
def pop(l):
    if is_empty():
        print("underflow")
    else:
        return l.pop()

print("STACK OPERATIONS  ")
print("1. Push an Element")
print("2. Pop an Element")
print("3. Print Stack")
print("4. Exit")
l=[]
while True:

    x=int(input("Enter choice: "))
    if x==1:
        n=input("Enter an element: ")
        push(l,n)
        print("Element pushed to stack")
    elif x==2:
        if is_empty(l):
            print("Stack Underflow")
        else:
            print("removed element is - ",l.pop())
    elif x==3:
        if is_empty(l):
            print("Empty stack")
        else:
            m=len(l)-1
            print(l[m],"<---------TOP")
            for i in range(len(l)-1-1,-1,-1):
                print(l[i])
    elif x==4:
        break
