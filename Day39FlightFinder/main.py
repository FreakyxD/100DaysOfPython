# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

# load sheet data
data_manger = DataManager()
flight_search = FlightSearch()
sheet_data = data_manger.get_sheet_content()["prices"]


# prepare IATA codes & update sheet row
rows_empty_iata = [city for city in sheet_data if len(city["iataCode"]) == 0]

for city in rows_empty_iata:
    row_id = city["id"]

    change_json = {
        "price": {
            "iataCode": flight_search.get_iata_codes()
        }
    }

    # send prepared data
    data_manger.update_sheet_row(row_id, change_json)
