def main():
    menu = """C - Convert Celsius to Fahrenheit 
F - Convert Fahrenheit to Celsius 
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    get_result(choice, menu)
    print("Thank you.")


def get_result(choice, menu):
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9.0
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()


main()
