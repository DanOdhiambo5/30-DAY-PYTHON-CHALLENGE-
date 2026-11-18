correct_password = "python123"

password = input("Enter password: ")

while password != correct_password:
    print("Wrong password. Try again.")
    password = input("Enter password: ")

print("Access granted!")


