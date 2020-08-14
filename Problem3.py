food = input("Enter Food Items In Increasing Order OF calories seperated by comma : ").split(",")
print(food)
print(list("Using Rev Method : ",reversed(food)))
print("Using Sliceing : ",food)
leng=len(food)
for i in range(leng//2):
    a=food[i]
    b=food[-i-1]
    food[i]=b
    food[-i-1]=a
    print(food)