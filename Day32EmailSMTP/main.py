import smtplib
from credentials import MY_EMAIL, MY_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT, TO_ADDRESS

# avoid connection.close()
with smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_ADDRESS,
        msg="Subject: My first subject\n\nJust an email body"
    )
