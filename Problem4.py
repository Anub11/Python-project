def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

inp=int(input("Enter no. : "))
num=[]
for i in range(inp):
    inp1=int(input("Enter no : "))
    num.append(inp1)
for i in num:
    print(
        f"Next palindrome for {i} is {next_palindrome(i)}")

