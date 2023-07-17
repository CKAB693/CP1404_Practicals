password = input("password: ")
while len(password) <= 0:
    print("Invalid password")
    password = input("password: ")
print(len(password) * "*")
"""the loop only execute when the password is nothing"""
