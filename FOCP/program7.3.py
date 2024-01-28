'''Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''
countries_and_capitals = {}

def add_country():
    country = input("Enter the name of a country: ").capitalize()
    countries_and_capitals[country] = input(f"Enter the capital city of {country}: ").capitalize()
    print(f"{country}'s capital city, {countries_and_capitals[country]}, has been added.")

def display_capital():
    country = input("Enter the name of a country: ").capitalize()
    print(f"The capital city of {country} is {countries_and_capitals.get(country, 'unknown')}.")

def main():
    while True:
        print("\nOptions:\n1. Add a new country and its capital\n2. Display the capital of a country\n3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1': add_country()
        elif choice == '2': display_capital()
        elif choice == '3': print("Goodbye!"); break
        else: print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
