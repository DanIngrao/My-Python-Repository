import os
from pathlib import *

route = Path('Proyects\\P6Proyect_KitchenRecipes\\Kitchen Recipes')
amount_recipes = len(list(route.glob('**/*.txt')))
amount_categories = len([r for r in route.iterdir() if route.is_dir()])

print(f'Welcome to the kitchen recipes app. Here you can find {amount_recipes} recipes and {amount_categories} categories.')