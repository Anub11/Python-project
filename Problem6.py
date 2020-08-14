import random
inp1=int(input("Enter 1st no: "))
inp2=int(input("Enter 2nd no: "))
answer = random.choice(range(inp1, inp2))
print(answer)
print("Play Player 1 : ")
c=0
c1=0
while 1:
    inp3=int(input("Enter Your no : "))
    if inp3>answer :
        print("Enter Less no ")
    elif inp3<answer :
        print("Enter greater no ")
    else:
        print(f"Congratulation !!! No of trials = {c}")
        break
    c+=1
print("Play Player 2 : ")
while 1:
    inp3=int(input("Enter Your no : "))
    if inp3>answer :
        print("Enter Less no ")
    elif inp3<answer :
        print("Enter greater no ")
    else:
        print(f"Congratulation !!! No of trials = {c1}")
        break
    c1+=1

if c1>c:
    print("Plaer 1 Win The game!!")
elif c1<c:
    print("Plaer 2 Win The game!!")
else:
    print("Draw!!")