# ------ Print -------
print("Anubhav ")
print("bej")
print("anubhav ", end=" ")
print("bej")
#----- variable -------
var1 = "hello"
print(var1)
var2="100"
var3="100"
print(int(var2) + int(var3))
print(var2)
print(type(var1))
print(10 * "hello\n")
#print("enter the no ")
#imp=input()
#print("you entered : ",int(imp)+10)
#--------String---------
mystr="Amunhaavv  sd a"
print(len(mystr))
print(mystr[9])
print(mystr[0:6])
print(mystr.isalnum()) #alfanumeric
print(mystr.endswith('a'))
print(mystr.count('a'))
print(mystr.find("vv"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("sd","uu"))
#----------list------------
grc = ["aa" , "ff" , "ff" , "sa" , 4]
print(grc[3])
num=[1 , 3 , 5 , 6 , 2 ]
num.sort()
num.remove()
print(num[0:3:])
num.append(32)
num.insert(2, 77)
num.remove(2)
num.pop()
num[1] = 44
tp=(1 , 5 , 8)
print(tp)
tp[1]=9 #touple is immutable
#swap logic in python
a = 10
b = 20
a , b = b , a
#-------------dictionary-----------------
d1 = {"Anub" : "bej" , "Rohan" : "Das" , "subh" : {"T": "a" , "Y" : "u"}
      }
d1["Ankit"] = "Kumar"
print(d1)
print(d1["Anub"])
print(d1["subh"]["T"])
del d1["Ankit"]
d2 = d1 #if we delete something from d1 it is also delete from d2
d2 = d1.copy()
print(d1.get("Anub"))
print(d1.update({"lena":"sing"}))
print(d2.keys())
print(d2.items())
#----------------set------------------
s = set()
l=[1, 3, 4, 5]
s_from_list = set(l)
print(s_from_list)
s.add(1)
s.add(2)
#s.add(1)#not add because set tacks only unique values
s1 = s.intersection({1,2,3})

#-----------------if else ---------------------

var1=10
var2=20

if var1>var2 :
    print("grater")
if var1==var2 :
    print("equal")
else:
    print("laser")

if var1>var2 :
    print("grater")
elif var1==var2:
    print("equal")
else:
    print("laser")
lis1 = [2, 6, 4]
if 2 in lis1 :
    print("YES")
if 22 not in lis1 :
    print("yes")

# ------------ LOOP ----------

  list1 = [ ["Harry", 1], ["Larry", 2], ["Carry", 6], ["Marie", 250] ]
 dict1 = dict(list1)

 for item in dict1:
     print(item)
 for item, lollypop in dict1.items():
     print(item, "and lolly is ", lollypop)
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

#----------- while loop --------------
i = 0
while i>20 :
    print(i)
    i = i+1

# ------------ break and continue --------------------

i = 0
while i>20 :
    print(i)
    if i==33 :
        break
    i = i + 1

inp = int(input("Enter the no : "))
while(1) :
    if inp >=100 :
        print("true")
        break
    else:
        print("False")

#---------------function-----------------

def function1():
    print("function")

def fun2(a,b):
    """This is avg function"""
    avg =(a/b)/2
    return avg
v=fun2(12,11)
print(v)
print(fun2.__doc__)

#----------------Exception Handeling ---------------
n4=input("Enter the no : ")
n5=print("Enter the no2 : ")
try:
    print("ADD ",int(n4)+int(n5))
except Exception as e:
    print(e)
print("BINGO!!!")

""" 
r : r mode opens a file for read only. We do not have the permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of file. It also does not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals the file data as a string.
b : b stands for binary and this mode can only open binary file, that are read in bytes. The binary files include images, documents or all other files that require specific software to be read.
+ : In plus mode we can read and write a file simultaneously. The mode is mostly use in cases where we want to update our file.
"""