# import random
#
# random_number = random.randint(0, 1)
# # print(random_number)
# rand = random.random() * 100
# # print(rand)
# lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
# choice = random.choice(lst)
# print(choice)
#
# import calendar
#
# print("Your Calender\n \n ")
#
# y = int(input("Enter the Year : "))
# m = int(input("Enter the month : "))
#
# mycalender = calendar.month(y , m)
# print("\n", mycalender)
#
# import math
#
# sol = math.factorial(5)
# print("Factorial: ", sol)
#
# import time
#
# print("This is printed immediately.")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds.")

import platform
x = platform.system()
print(x)

import math
square = math.sqrt(25)
print(square)

#-------time module----------

import time

initial = time.time()

k = 0
while (k < 45):
    print("This is harry bhai")
    time.sleep(2)
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)


