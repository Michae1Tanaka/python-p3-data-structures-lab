from operator import attrgetter

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    food_name = [foods.get("name") for foods in spicy_foods]
    return food_name


def get_spiciest_foods(spicy_foods):
    sorted_spicy_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return sorted_spicy_foods


def print_spicy_foods(spicy_foods):
    emoji = "🌶"
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji * food['heat_level']}"
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    spiciness_levels = [foods.get("heat_level") for foods in spicy_foods]
    average = sum(spiciness_levels) // len(spiciness_levels)
    return average


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
