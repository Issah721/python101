print("Welcome to the signup page❤️!")

name = input("What's your name? ")

name = name.strip()

if len(name) == 0:
    print("You didn't enter a name. Please try again.")
else:
    print(f"Hello, {name}")


