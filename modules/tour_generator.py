def generate_foodie_tour(city, weather, dining_type, dishes, restaurants):
    narrative = f"Weather today in {city}: {weather} (recommended {dining_type} dining)\n"
    meals = ["Breakfast", "Lunch", "Dinner"]
    for i, meal in enumerate(meals):
        dish = dishes[i % len(dishes)]
        rest = restaurants.get(dish)
        if not rest:
            continue
        narrative += f"\n🍽️ {meal}:\nEnjoy {dish} at {rest['name']} located at {rest['address']}.\n"
        narrative += f"This top-rated spot ({rest['rating']}⭐) offers a great {dining_type} setting.\n"
    return narrative
