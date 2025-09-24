from tripdata import get_trip
from datetime import datetime
import json

trips = [
    get_trip("Paris", "15-05-2022", "Visited the Eiffel Tower"),
    get_trip("Rome", "20-06-2022", "Saw the Colosseum"),
    get_trip("Tokyo", "01-12-2023", "Enjoyed sushi at Tsukiji")
]

for trip in trips:
    date = datetime.strptime(trip["date"], "%d-%m-%Y")   
    trip["date"] = date.strftime("%B %d, %Y")

tripsjson = json.dumps(trips, indent=2)   

print(tripsjson)
