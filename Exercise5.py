import datetime
def gettime():
    return datetime.datetime.now()

while 1 :
    inp=int(input("Press 1 for lock\nPress 2 for retrive\nPress 3 for Quit \nEnter Your Choice : "))

    if inp==1:

        inp2=int(input("Press 1 for lock Food\nPress 2 for lock Exercise\nEnter Your Choice : "))

        if inp2==1:

            inp3=int(input("Press 1 for lock Food for A\nPress 2 for lock Food for B\nPress 3 for lock Food for C\nEnter Your Choice : "))
            if inp3==1:
                val=input("Type here .....\n")
                with open("A-FOOD.txt",'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            elif inp3==2:
                val=input("Type here .....\n")
                with open("B-FOOD.txt",'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            elif inp3==3:
                val=input("Type here .....\n")
                with open("C-FOOD.txt",'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            else:
                print("Wrong Input!!")

        if inp2 == 2:

            inp3 = int(input("Press 1 for lock Exe for A\nPress 2 for lock Exe for B\nPress 3 for lock Exe for C\nEnter Your Choice : "))
            if inp3 == 1:
                val = input("Type here .....\n")
                with open("A-Exe.txt", 'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            elif inp3 == 2:
                val = input("Type here .....\n")
                with open("B-Exe.txt", 'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            elif inp3 == 3:
                val = input("Type here .....\n")
                with open("C-Exe.txt", 'a') as op:
                    op.write(str([str(gettime())]) + " : " + val + "\n")
                print("Successfully lock Food----")

            else:
                print("Wrong Input!!")

    elif inp == 2:

        inp2 = int(input("Press 1 for retrive Food\nPress 2 for retive Exercise"))

        if inp2 == 1:

            inp3 = int(input("Press 1 for retrive Food for A\nPress 2 for retrive Food for B\nPress 3 for retrive Food for C\nEnter Your Choice : "))
            if inp3 == 1:
                with open("A-FOOD.txt", 'r') as op:
                    for i in op:
                        print(i,end=" ")
                print("Successfully retrive Food----")

            elif inp3 == 2:
                with open("B-FOOD.txt", 'r') as op:
                    for i in op:
                        print(i, end=" ")
                print("Successfully retrive Food----")

            elif inp3 == 3:
                with open("C-FOOD.txt", 'r') as op:
                    for i in op:
                        print(i, end=" ")
                print("Successfully retrive Food----")
            else:
                print("Wrong Input!!")

        if inp2 == 2:

            inp3 = int(input("Press 1 for RET Exe for A\nPress 2 for RET Exe for B\nPress 3 for RET Exe for C\nEnter Your Choice : "))
            if inp3 == 1:
                with open("A-Exe.txt", 'r') as op:
                    for i in op:
                        print(i, end=" ")
                print("Successfully retrive EXE----")
            elif inp3 == 2:
                with open("B-Exe.txt", 'r') as op:
                    for i in op:
                        print(i, end=" ")
                print("Successfully retrive EXE----")
            elif inp3 == 3:
                with open("C-Exe.txt", 'r') as op:
                    for i in op:
                        print(i, end=" ")
                print("Successfully retrive EXE----")
            else:
                print("Wrong Input!!")

    elif inp==3:
        break

    else:
        print("Wrong Input!!!")

print("Thanks For Using!")
