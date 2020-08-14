inp=int(input("Enter the no of rows : "))
val=input("Eneter true or false : ")
if val == 'true' :
    for i in range(1,inp+1):
        for j in range(1,i+1):
            print("* ",end=" ")
        print()
elif val == 'false' :
    for i in range(inp,0,-1):
        for j in range(1,i+1):
            print("* ",end=" ")
        print()
else :
    print("wrong Choice")