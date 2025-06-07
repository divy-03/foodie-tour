# app.py
import streamlit as st
from modules.weather import get_weather_condition
from modules.dishes import get_iconic_dishes
from modules.restaurants import find_top_restaurants
from modules.tour_generator import generate_foodie_tour

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
