class libary :
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.landDict={}

    def Display(self):
        print(f"-------- Welcome To {self.name} -------------\n")
        print("Books : \n")
        for i in self.booklist:
           print(i,"\n")


    def landBook(self,user,book):
        if book not in self.landDict.keys():
            self.landDict.update({book:user})
            print(f" {user} You Can Take your {book} Book ")
        else:
            print(f"Book hasbeen taken by : {self.landDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print(f"----------- {book} Added ---------")

    def returnBook(self, book):
        self.landDict.remove(book)

if __name__ == '__main__':
    harry = libary(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],
                    "CodeWithHarry")

    while (True):
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.Display()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.landBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue