
while(1):

    inp1 = int(input("Enter 1st no : "))
    inp2 = int(input("Enter 2nd no : "))
    inp3 = input("Enter Operator (+,-,/,*,%) And press q for Exit : ")

    if inp1==45 and inp2==3 and inp3=='*' :
        print("555")
    elif inp1==56 and inp2==9 and inp3=='+' :
        print("77")
    elif inp1==56 and inp2==6 and inp3=='/' :
        print("4")
    elif inp3=='+' :
        print("Sum = ",inp1+inp2)
    elif inp3=='-' :
        print("Sub = ",inp1-inp2)
    elif inp3=='/' :
        print("div = ",inp1/inp2)
    elif inp3=='*' :
        print("Sum = ",inp1*inp2)
    elif inp3=='%' :
        print("Mod = ",inp1%inp2)
    elif inp3=='q':
        break
    else:
        print("Wrong input")

