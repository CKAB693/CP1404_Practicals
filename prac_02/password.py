def main():
    password = input("password: ")
    get_password(password)


def get_password(password):
    while len(password) <= 0:
        print("Invalid password")
        password = input("password: ")
    print(len(password) * "*")


"""the loop only execute when the password is nothing"""

main()
