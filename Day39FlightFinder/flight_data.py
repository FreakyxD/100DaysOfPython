from datetime import datetime, timedelta


class FlightData:
    # This class is responsible for structuring the flight data.

    def structure_flight_data(self, flight_data_dict):
        flight_data = flight_data_dict["data"][0]

        # departure date
        departure_date_ts = flight_data["dTime"]
        departure_date = datetime.fromtimestamp(departure_date_ts)
        departure_date_formatted = departure_date.strftime("%d/%m/%Y")

        # arrival date
        arrival_date = departure_date + timedelta(days=flight_data["nightsInDest"])
        arrival_date_formatted = arrival_date.strftime("%d/%m/%Y")

        return {
            "dep_airport_iata": flight_data["flyFrom"],
            "dest_airport_iata": flight_data["flyTo"],
            "departure_city": flight_data["cityFrom"],
            "destination_city": flight_data["cityTo"],
            "price": flight_data["price"],
            "flight_dep_date": departure_date_formatted,
            "flight_arr_date": arrival_date_formatted,
        }
