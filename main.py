import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

print("welcome to the password generator")
h_letters = int(input("how many letters would you like in your password\n"))
h_numbers = int(input("how many numbers would you like in your password\n"))
h_symbols = int(input("how many symbols would you like in your password\n"))

# hard level
password_list = []

for let in range(1, h_letters + 1):
    password_list.append(random.choice(letters))

for num in range(1, h_numbers + 1):
    password_list += random.choice(numbers)


for sym in range(1, h_symbols + 1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(f"your new generated password is {password_list}")
password = ""
for let in password_list:
    password += let
print(f"your password joined together is {password} . please keep it safe ")



