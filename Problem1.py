inp=int(input("Enter age or year : "))
age=0
year=0
if inp>0 and inp<120 :
    age=inp
elif inp>120 and inp<1901:
    print("Feeling Sad ! Now this time the peoples born in this year of birth is not alive")
    
elif inp>1900 and inp<2020:
   year=inp
else:
    print("You are not born yet so don't be oversmart!")

if age>104:
    print("Most oldest Person ::::- ")
if len(str(inp))==2 or len(str(inp))==3:
    cal_age=100-age
    print("You becane 100 years after : ",cal_age)

elif len(str(inp)) == 4 :
    cal_yer=year+100
    print("You becane 100 years in year : ", cal_yer)

print("Can you want to see your age at some particular year?")
optionally = input('Please input yes or no only : ')
if optionally == 'yes':
    year1 = int(input('Enter the particular year : '))
    if age:
       print(f'You are {(year1-2019) + age} old in {year}')
    else:
       print(f'you are {year1 - year} old in {year1}')
