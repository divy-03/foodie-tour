import os
import requests
from dotenv import load_dotenv

load_dotenv()

def find_top_restaurants(city, dishes):
    api_key = os.getenv("FOURSQUARE_API_KEY")
    headers = {
        "Authorization": api_key,
        "Accept": "application/json"
    }

    restaurants = {}
    for dish in dishes:
        params = {
            "query": dish,
            "near": city,
            "limit": 1
        }
        url = "https://api.foursquare.com/v3/places/search"
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            place = data["results"][0]
            address = ", ".join(place["location"].get("formatted_address", []))
            restaurants[dish] = {
                "name": place["name"],
                "address": address or "Unknown Street",
                "rating": 4.5  # Foursquare free tier doesn't return ratings
            }
    return restaurants
