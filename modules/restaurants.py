# modules/restaurants.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def find_top_restaurants(city, dishes, dining_type):
    api_key = os.getenv("YELP_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    restaurants = {}
    for dish in dishes:
        url = f"https://api.yelp.com/v3/businesses/search?term={dish}&location={city}&limit=1&sort_by=rating"
        response = requests.get(url, headers=headers)
        data = response.json()
        if "businesses" in data and data["businesses"]:
            business = data["businesses"][0]
            restaurants[dish] = {
                "name": business["name"],
                "address": ", ".join(business["location"]["display_address"]),
                "type": dining_type,
                "rating": business.get("rating", 4.5)
            }
    return restaurants
