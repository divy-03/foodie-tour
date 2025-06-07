# --- Imports and Setup ---
import requests
import os
from dotenv import load_dotenv
import streamlit as st

st.set_page_config(page_title="Foodie Tour Generator", page_icon="🍽️")  # <-- FIRST Streamlit command

load_dotenv()

def get_weather_condition(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if "weather" in data:
        return data["weather"][0]["main"]
    return "Clear"

# --- Dishes Module ---
city_dish_map = {
    "Bangkok": ["Pad Thai", "Tom Yum Goong", "Mango Sticky Rice"],
    "Barcelona": ["Paella", "Tapas", "Crema Catalana"],
    "Tokyo": ["Sushi", "Ramen", "Mochi"]
}
def get_iconic_dishes(city):
    return city_dish_map.get(city, ["Local Specialty"])

# --- Restaurants Module ---
def find_top_restaurants(city, dishes, dining_type):
    api_key = os.getenv("YELP_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    restaurants = {}
    for dish in dishes:
        url = f"https://api.yelp.com/v3/businesses/search?term={dish}&location={city}&limit=1&sort_by=rating"
        response = requests.get(url, headers=headers)
        data = response.json()
        if "businesses" in data and len(data["businesses"]) > 0:
            business = data["businesses"][0]
            restaurants[dish] = {
                "name": business["name"],
                "address": ", ".join(business["location"]["display_address"]),
                "type": dining_type,
                "rating": business.get("rating", 4.5)
            }
    return restaurants

# --- Tour Generator Module ---
def generate_foodie_tour(city, weather, dining_type, dishes, restaurants):
    narrative = f"Weather today in {city}: {weather} (recommended {dining_type} dining)\n"
    meals = ["Breakfast", "Lunch", "Dinner"]
    for i, meal in enumerate(meals):
        dish = dishes[i % len(dishes)]
        if dish not in restaurants:
            continue
        rest = restaurants[dish]
        narrative += f"\n🍽️ {meal}:\nEnjoy {dish} at {rest['name']} located at {rest['address']}.\n"
        narrative += f"This top-rated spot ({rest['rating']}⭐) offers a great {dining_type} setting.\n"
    return narrative

# Streamlit Web Interface

st.set_page_config(page_title="Foodie Tour Generator", page_icon="🍽️")
st.title("🍴 One-Day Foodie Tour Generator")

city_input = st.text_input("Enter a city:")

if st.button("Generate Tour") and city_input:
    city = city_input.title()
    weather = get_weather_condition(city)
    dining_type = "outdoor" if weather in ["Clear", "Sunny", "Partly Cloudy"] else "indoor"
    dishes = get_iconic_dishes(city)
    restaurant_data = find_top_restaurants(city, dishes, dining_type)
    tour_narrative = generate_foodie_tour(city, weather, dining_type, dishes, restaurant_data)
    st.text(tour_narrative)
    
    # --- Main Execution Block ---
cities = ["Bangkok", "Barcelona", "Tokyo"]

for city in cities:
    print(f"\n🍴 Foodie Tour for {city} 🍴")
    weather = get_weather_condition(city)
    dining_type = "outdoor" if weather in ["Clear", "Sunny", "Partly Cloudy"] else "indoor"
    dishes = get_iconic_dishes(city)
    restaurant_data = find_top_restaurants(city, dishes, dining_type)
    tour_narrative = generate_foodie_tour(city, weather, dining_type, dishes, restaurant_data)
    print(tour_narrative)
    
    code = st.set_page_config(page_title="Foodie Tour Generator", page_icon="🍽️")
st.title("🍴 One-Day Foodie Tour Generator")

city_input = st.text_input("Enter a city:")

if st.button("Generate Tour") and city_input:
    city = city_input.title()
    weather = get_weather_condition(city)
    dining_type = "outdoor" if weather in ["Clear", "Sunny", "Partly Cloudy"] else "indoor"
    dishes = get_iconic_dishes(city)
    restaurant_data = find_top_restaurants(city, dishes, dining_type)
    tour_narrative = generate_foodie_tour(city, weather, dining_type, dishes, restaurant_data)
    st.text(tour_narrative)
with open("julepai.py", "w", encoding="utf-8") as f:
    f.write(code)

