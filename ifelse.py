print("Welcome to the signup page❤️!")

name = input("What's your name? ")

name = name.strip()

if len(name) == 0:
    print("You didn't enter a name. Please try again.")
else:
    print(f"Hello, {name}")


print(f"Hello, {name}, would you like some food? ")
input = input("yes/no: ").strip().lower()
if input == "yes":
    print("Here is some food 🍕")
else :
    print("Okay, no food for you then 😢")