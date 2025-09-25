#ask user for their name
name = input("What's your name? ")

name = name.strip()


#say hello to user
print(f"Hello, {name}")
age = input("what is your age? ")
print(f"{name} is {age} years old")

#calculate area of rectangle
length = float (int(input("Enter the length of the rectangle: ")))
width = float(int(input("Enter the width of the rectangle: ")))

import functions101
area = functions101.my_rect_area(length , width)
print(f"The area of the rectangle is {area} square units.")

#Check user age, if they are 15 or older, they can continue signing up
if int(age) >= 15:
    print("You are old enough to continue.")
else:
    print("You are not old enough to continue.")