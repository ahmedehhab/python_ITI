
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


######################################################################
age = input("enter age ")
while not age.isdigit():
    age = input("enter a valid age ")
age = int(age)

have_coupon_input = input("Do you have a coupon? ").lower()
while have_coupon_input not in ["yes", "no"]:
    have_coupon_input = input("enter 'yes' or 'no' ").lower()
have_coupon = have_coupon_input == "yes"

if age < 18 or age > 65 or have_coupon:
    print("true")
else:
    print("false")

##################################################################
name = input("Enter your name: ")
while name == "":
    name = input("enter your name ")

greeting = "Hello, " + name + "!"
print(greeting)

###################################################################
full_name = input("enter full name ")
while len(full_name.split()) < 2:
    full_name = input("Please enter a fullname ")

names = full_name.split()
first_initial = names[0][0]
last_initial = names[-1][0]

print(first_initial + last_initial)

#################################################################
name = input("enter name ")
while name == "":
    name = input("enter name: ")

age = input("enter age: ")
while not age.isdigit():
    age = input("Please enter a valid age ")

sentence = "{} is {} years old."
finalSentence = sentence.format(name, age)
print(f"{name} is {age} years old")
print(finalSentence)