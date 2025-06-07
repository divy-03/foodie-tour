import streamlit as st
from modules.weather import get_weather_condition
from modules.dishes import get_iconic_dishes
from modules.restaurants import find_top_restaurants
from modules.tour_generator import generate_foodie_tour

st.set_page_config(page_title="Foodie Tour Generator", page_icon="🍽️")

st.title("🍴 One-Day Foodie Tour Generator")
city_input = st.text_input("Enter a city (e.g., Bangkok, Barcelona, Tokyo):")

if st.button("Generate Tour") and city_input:
    city = city_input.title()
    weather = get_weather_condition(city)
    dining_type = "outdoor" if weather in ["Clear", "Sunny", "Partly Cloudy"] else "indoor"
    dishes = get_iconic_dishes(city)
    restaurants = find_top_restaurants(city, dishes)
    tour_narrative = generate_foodie_tour(city, weather, dining_type, dishes, restaurants)
    st.text(tour_narrative)
