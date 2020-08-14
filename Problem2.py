inp=int(input("Enter The no of Apple : "))
inp1=int(input("Enter The no of Min : "))
inp2=int(input("Enter The no of Max : "))



while inp1<inp2 :

    if inp%inp1==0:
        print(f"{inp1} is a divisor of {inp}")
    inp1+=1
