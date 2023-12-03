from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data_manger = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
sheet_data = data_manger.get_sheet_content()["prices"]

# prepare IATA codes & update sheet row
rows_empty_iata = [city for city in sheet_data if len(city["iataCode"]) == 0]

for city in rows_empty_iata:
    row_id = city["id"]

    change_json = {
        "price": {
            "iataCode": flight_search.get_iata_codes(city["city"])
        }
    }

    # send prepared data
    data_manger.update_sheet_row(row_id, change_json)

# get the cheapest flight for city from sheet
for city in sheet_data:
    flight_data_dict = flight_search.get_cheapest_flight(city["iataCode"])
    flight_price = flight_data_dict["data"][0]["price"]
    sheet_price = city["lowestPrice"]

    if flight_price < sheet_price:
        # push new price to sheet
        row_id = city["id"]

        change_json = {
            "price": {
                "lowestPrice": flight_price
            }
        }

        data_manger.update_sheet_row(row_id, change_json)

        # send structured dict to notification_manager IF price lower than on sheet
        formatted_flight_data = flight_data.structure_flight_data(flight_data_dict)
        notification_manager.send_formatted_flight_data_to_telegram(formatted_flight_data)
