import random

Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '*']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("This is a Password Generator")

user_input1 = int(
    input("Enter the numbers of Alphabets that you want in your password: "))
user_input2 = int(
    input("Enter the numbers of Symbols that you want in your password: "))
user_input3 = int(input("Enter the Numbers that you want in your password: "))

password_list = []

for i in range(1, user_input1+1):
    char = random.choice(Alphabets)
    password_list += char


for i in range(1, user_input2+1):
    sym = random.choice(Symbols)
    password_list += sym

for i in range(1, user_input3+1):
    num = random.choice(Numbers)
    password_list += num

random.shuffle(password_list)


password = ""

for characters in password_list:
    password += characters

print(f"The Password is: {password}")
