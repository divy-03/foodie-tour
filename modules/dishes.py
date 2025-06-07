city_dish_map = {
    "Bangkok": ["Pad Thai", "Tom Yum Goong", "Mango Sticky Rice"],
    "Barcelona": ["Paella", "Tapas", "Crema Catalana"],
    "Tokyo": ["Sushi", "Ramen", "Mochi"]
}

def get_iconic_dishes(city):
    return city_dish_map.get(city, ["Local Specialty"])
