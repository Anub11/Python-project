import random
choice=["Stone","paper","scissor"]
n=10
u=0
c=0
while  n>1:
    com_c=random.choice(choice)
    inp=input("Entrt your choice (Stone,paper,scissor) : ")
    if com_c==inp :
        print("Draw")

    elif com_c=='stone' and inp=='paper' :
        print("You Win !")
        u=u+1

    elif com_c=='paper' and inp=='Stone' :
        print("You Lose !")
        c=c+1

    elif com_c=='scissor' and inp=='stone' :
        print("You Win !")
        u=u+1

    elif com_c=='stone' and inp=='Scissor' :
        print("You lose !")
        c=c+1

    elif com_c=='scissor' and inp=='paper' :
        print("You lose !")
        c=c+1

    elif com_c == 'paper' and inp == 'scissor':
        print("You win !")
        u = u + 1

    else:
        print("Enter valid Choice")
        continue

    n=n-1
    print(f"You have {n} chance ")

if u > c:
    print("You Win the Game ! \n"
          f"Computer Point {c}  Your point {u}")
elif c > u:
    print("You Loose The Game !!"
          f"Computer Point {c}  Your point {u}")
else:
    print("Draw match")

