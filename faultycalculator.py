while(1):
    print("Enter 1st no : ")
    in1 = int(input())
    print("Enter 2nd no : ")
    in2 = int(input())
    print("Chose operator + - * / otherwise press n to break ")
    op = input()
    if(op=='*') and (in1==45) and (in2==3) :
        print("555")
    elif (op=='+') and (in1==56) and (in2==9) :
        print("77")
    elif (op=='/') and (in1==56) and (in2==6) :
        print("4")
    elif op=='+':
        print("RESULT : ",in1+in2)
    elif op == '-':
        print("RESULT : ", in1 - in2)
    elif op == '*':
        print("RESULT : ", in1 * in2)
    elif op == '/':
        print("RESULT : ", in1 / in2)
    elif (op=="break"):
        break
    else:
        print("INVALID")

