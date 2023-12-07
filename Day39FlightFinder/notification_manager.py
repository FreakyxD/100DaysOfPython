from Day0UsefulCode.TelegramBot.main import TelegramBot
import smtplib
from auth import MY_EMAIL, MY_EMAIL_PASSWORD, SMTP_SERVER, SMTP_SERVER_PORT


class NotificationManager(TelegramBot):
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        super().__init__()

    def send_formatted_flight_data_to_telegram(self, flight_data_dict):
        price = flight_data_dict["price"]
        dep_city = flight_data_dict["departure_city"]
        dep_city_iata = flight_data_dict["dep_airport_iata"]
        dest_city = flight_data_dict["destination_city"]
        dest_city_iata = flight_data_dict["dest_airport_iata"]
        dep_date = flight_data_dict["flight_dep_date"]
        arr_date = flight_data_dict["flight_arr_date"]

        ready_string = (f"Low price alert! Only €{price} to fly from {dep_city}-{dep_city_iata} to "
                        f"{dest_city}-{dest_city_iata}, from {dep_date} to {arr_date}.")
        super().send_message_to_telegram_bot(ready_string)

    def send_emails(self, flight_data_dict, customer_data):
        price = flight_data_dict["price"]
        dep_city = flight_data_dict["departure_city"]
        dep_city_iata = flight_data_dict["dep_airport_iata"]
        dest_city = flight_data_dict["destination_city"]
        dest_city_iata = flight_data_dict["dest_airport_iata"]
        dep_date = flight_data_dict["flight_dep_date"]
        arr_date = flight_data_dict["flight_arr_date"]

        emails = [customer["email"] for customer in customer_data]


        with smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Low price alert!\n\nOnly €{price} to fly from {dep_city}-{dep_city_iata} to "
                        f"{dest_city}-{dest_city_iata}, from {dep_date} to {arr_date}."
                )
