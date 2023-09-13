#!/usr/bin/env python3

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
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    max_heat_level = max(food["heat_level"] for food in spicy_foods)
    return [food for food in spicy_foods if food["heat_level"] == max_heat_level]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        emojis = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
