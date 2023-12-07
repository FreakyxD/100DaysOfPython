from sheety import post_new_row

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

# emails must match
match = False
while not match:
    email = input("What is your email?\n")
    email_control = input("Type your email again.\n")
    if email == email_control:
        match = True
    else:
        print("Emails don't match.")

if post_new_row(first_name, last_name, email) != 200:
    print("Something didn't work.")
else:
    print("You're in the club!")
