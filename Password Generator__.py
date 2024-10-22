letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
alpha=int(input("Enter the number of letters you want in your password : "))
num=int(input("Enter the number of numbers you want in your password : "))
sym=int(input("Enter the number of characters you want in your password :"))
password=[]
for i in range(alpha):
    password.append(random.choice(letters))
for i in range(num):
    password.append(random.choice(numbers))
for i in range (sym):
    password.append(random.choice(symbols))
random.shuffle(password)
s=""
for i in password:
    s+=i
print(f"Your password is {s}")
