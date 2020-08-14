import random

def fun2(num):
    fak_lst=[]
    i1=random.choice(range(2,10))
    for i in range(1,11):
        if i==i1 :
            i3 = random.choice(range(2, 110))
            fak_lst.append(i3 * num)
        else:
            fak_lst.append(i*num)
    return (fak_lst)

def fun1(num,lst):

    org_lst=[]
    for i in range(1,11):
        org_lst.append(i*num)
    print("Original : ",org_lst)
    for i in range(len(org_lst)):
            if org_lst[i]!=lst[i]:
                print(f"Wrong{i+1} value {lst[i]}")


if __name__ == '__main__':
    inp=int(input("Enter No : "))
    table=fun2(inp)
    print("Fake List : ",table)
    fun1(inp,table)
