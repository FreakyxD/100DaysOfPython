

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

# emails must match
match = False
while not match:
    email = input("What is your email?\n")
    email_control = input("Type your email again.\n")
    if email == email_control:
        match = True
        print("You're in the club!")
    else:
        print("Emails don't match.")
