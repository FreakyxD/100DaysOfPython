import smtplib
from credentials import MY_EMAIL, MY_PASSWORD, SMTP_SERVER, TO_ADDRESS

connection = smtplib.SMTP(SMTP_SERVER)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS)
connection.close()