no=34
print("YOU GUESS ONLY 9 TIMES \n")
n=9
while(n>=0) :
    ch=int(input("Enter your no : "))
    if ch>no :
        print("choose less no.")
    elif ch<no :
        print("choose grter no")
    else:
        print("YOU WON !!!! ")
        break
    n=n-1
    print("CHOICE LEFT : ",n)
    if n==0 :
        print("GAME OVER!!")
        break



