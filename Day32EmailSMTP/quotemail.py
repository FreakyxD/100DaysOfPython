import smtplib
from auth import MY_EMAIL, MY_EMAIL_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT, TO_ADDRESS
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()  # 0 is Monday

# run only Tuesday
if day_of_week == 1:
    print("Today is Tuesday, executing...")
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
else:
    print("Today is not Tuesday, try again later...")
    quit()

# pick random quote
random_quote = random.choice(quotes)

# send email
with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_SERVER_PORT) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_ADDRESS,
        msg=f"Subject: Quote of the (Tues)day\n\n {random_quote}"
    )
