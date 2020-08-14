def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    if n>10:
        n = n+1
        while not is_palindrome(n):
            n += 1
        return n
    else:
        return n

inp=int(input("Enter no. : "))
num=[]
for i in range(inp):
    inp1=int(input("Enter no : "))
    num.append(inp1)
num1=[]
for i in num:
    num1.append(next_palindrome(i))
print(num1)