MINIMUM_NUMBER = 0


def main():
    password = validate_input()
    print_asterisks(password)


def validate_input():
    """identified the user input"""
    password = input("password: ")
    while len(password) <= MINIMUM_NUMBER:
        print("Invalid password")
        password = input("password: ")
    return password


def print_asterisks(password):
    """print asterisks"""
    print(len(password) * "*")


"""the loop only execute when the password is nothing"""

main()
