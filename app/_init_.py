import requests
from urllib.parse import urlencode

#distance matrix function that accepts two sets of coordinates {latitude, longitude}, then utilizes TrueWay Matrix API to compute distances (in meters) and travel duration times between those two locations (assuming user is driving a car)
def distance_matrix(origin, destination):

    #conversion factor = meters/mile
    meter_to_mile = 1609.34

    response = requests.get(
        "https://trueway-matrix.p.rapidapi.com/CalculateDrivingMatrix",
        params={"origins": f'{origin["lat"]},{origin["lng"]}', "destinations": f'{destination["lat"]},{destination["lng"]}'},
        headers={
            "x-rapidapi-key": "1b3e17da97msh8784bd378de9d66p17b153jsn255eb2ee1914",
		    "x-rapidapi-host": "trueway-matrix.p.rapidapi.com"
        }
    )

    data = response.json()

    commute = {
        #for one location coordinate pair {lat, lng}, response is in the form of a 2D array ("distances" in meters or "durations" in seconds) with distance/durations values at position [0][0]
        "commute_distance": round(data["distances"][0][0]/meter_to_mile, 2),
        "commute_time": round(data["durations"][0][0]/60, 2)
    }

    #return commute distance in miles and time in minutes rounded to two decimal places
    return commute


#function that accepts an address string, then uses the TrueWay Geocoding API to convert the address string into map coordinates {latitude, longitude}
def geo_code(address_to_convert):

    #https://urllib3.readthedocs.io/en/latest/user-guide.html use urlencode from urllib.parse package, convert address string to a query parameter for the request
    encoded_address = urlencode({"address": "85 10th Ave, New York, NY 10011"})

    response = requests.get(
        f'https://trueway-geocoding.p.rapidapi.com/Geocode?{encoded_address}&language=en',
        headers={
            "x-rapidapi-key": "1b3e17da97msh8784bd378de9d66p17b153jsn255eb2ee1914",
		    "x-rapidapi-host": "trueway-geocoding.p.rapidapi.com"
        }
    )

    data = response.json()

    #return {"latitute": ..., "longitute": ...} dictionary
    return data["results"][0]["location"]

