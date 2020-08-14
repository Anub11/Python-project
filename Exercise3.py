no=22
print("You have 5 times to guess!")
n=5
while n>=1 :
    inp = int(input("Enter your no : "))
    if no>inp :
        print("You entered grater")
    elif no<inp :
        print("You entered less")
    else:
        print("You Win !!!")
        break
    n=n-1
    if n==0 :
        print("Game Over!!")
    else:
        print(f"You have {n} no of guess")
