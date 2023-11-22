from auth import MY_EMAIL, MY_EMAIL_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT
from datetime import datetime
import smtplib
import pandas as pd
import random

# csv input format:
# name,email,year,month,day
# Test,test@email.com,1961,12,21
df = pd.read_csv("birthdays.csv")
birthday_dict = df.to_dict("records")


def generate_letter(recipient):
    recipient_name = recipient["name"]

    # pick random letter number
    l_number = random.randint(1, 3)

    with open(f"letter_templates/letter_{l_number}.txt", mode="r") as letter:
        prepared_letter = letter.read().replace("[NAME]", recipient_name)
        return prepared_letter


def send_letter(letter_text, recipient):
    with smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient,
            msg=f"Subject: Happy Birthday!\n\n{letter_text}"
        )


# Check if today matches a birthday in the birthdays.csv
today_tuple = (datetime.now().month, datetime.now().day)

for person_dict in birthday_dict:
    birthday_tuple = (person_dict["month"], person_dict["day"])
    recipient_email = person_dict["email"]

    if birthday_tuple == today_tuple:
        final_letter = generate_letter(person_dict)
        send_letter(final_letter, recipient_email)
