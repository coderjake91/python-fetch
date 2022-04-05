import pytest
import requests
from _init_ import distance_matrix, geo_code, search_listings


##faux user data simulating input from the application form
testData = {
    ##simulating the user's work address
    "origin": {
        "lat": "40.74334317912754",
        "lng": "-74.00767199382838",
        "area_code": "10011",
        "city": "New York",
        "state": "NY",
        "address": "85 10th Ave, New York, NY 10011",
    },
    ##simulating a 'chosen' apartment
    "destination": {
        "lat": "41.30731428096317",
        "lng": "-72.93124268296455",
        "area_code": "06511",
        "city": "New Haven",
        "state": "CT",
        "address": "274 Crown St, New Haven, CT 06511"
    },
    "searchParams": {
        "search_radius": 20,
        "response_limit": 15
    }
}

def test_distance_matrix():
    commute = distance_matrix(testData["origin"],testData["destination"])

    assert commute["commute_distance"] >= 0
    assert commute["commute_time"] >= 0

def test_geo_code():
    location = geo_code(testData["origin"]["address"])

    assert type(location["lat"]) == float
    assert type(location["lng"]) == float

def test_search_listings():
    apartment_listings = search_listings(testData["origin"]["area_code"], 
                                        testData["origin"]["state"], 
                                        testData["origin"]["state"], 
                                        testData["searchParams"]["search_radius"],
                                        testData["searchParams"]["response_limit"])
    
    assert len(apartment_listings) == testData["searchParams"]["response_limit"]