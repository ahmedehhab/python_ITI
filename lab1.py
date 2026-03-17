number = int(input("enter the number "))
start = int(input("enter the start "))
end = int(input("enter the end "))

if number >= start and number <= end:
    print("true")
else:
    print("false")




age = int(input("enter age "))
have_coupon = False

if age < 18 or age > 65 or have_coupon == True:
    print("true")
else:
    print("false")


name = input("enter your name ")

greeting = "Hello, " + name + "!"
print(greeting)


full_name = input("enter full name ")

names = full_name.split()

first_initial = names[0][0]
last_initial = names[-1][0]

print(first_initial + last_initial)



name = input("enter name ")
age = input("enter age ")

sentence = "{} is {} years old"
finalSentence=sentence.format(name, age)
print(f"{name} is {age} years old")
print(finalSentence)







number = input("enter the number ")
while not number.isdigit():
    number = input("enter a valid number ")
number = int(number)

start = input("enter the start ")
while not start.isdigit():
    start = input("enter a valid number ")
start = int(start)

end = input("enter the end ")
while not end.isdigit():
    end = input("enter a valid number ")
end = int(end)

if start <= number <= end:
    print("true")
else:
    print("false")



# Task 2: Discount eligibility
age = input("Enter age: ").strip()
while not age.isdigit():
    age = input("Please enter a valid age: ").strip()
age = int(age)

have_coupon_input = input("Do you have a coupon? (yes/no): ").strip().lower()
while have_coupon_input not in ["yes", "no"]:
    have_coupon_input = input("Please enter 'yes' or 'no': ").strip().lower()
have_coupon = have_coupon_input == "yes"

if age < 18 or age > 65 or have_coupon:
    print("true")
else:
    print("false")

print("\n---\n")

# Task 3: Greeting
name = input("Enter your name: ").strip()
while name == "":
    name = input("Name cannot be empty. Enter your name: ").strip()

greeting = "Hello, " + name + "!"
print(greeting)

print("\n---\n")

# Task 4: Initials
full_name = input("Enter full name: ").strip()
while len(full_name.split()) < 2:
    full_name = input("Please enter at least first and last name: ").strip()

names = full_name.split()
first_initial = names[0][0]
last_initial = names[-1][0]

print(first_initial + last_initial)

print("\n---\n")

# Task 5: Sentence with format
name = input("Enter name: ").strip()
while name == "":
    name = input("Name cannot be empty. Enter name: ").strip()

age = input("Enter age: ").strip()
while not age.isdigit():
    age = input("Please enter a valid age: ").strip()

sentence = "{} is {} years old."
finalSentence = sentence.format(name, age)
print(finalSentence)