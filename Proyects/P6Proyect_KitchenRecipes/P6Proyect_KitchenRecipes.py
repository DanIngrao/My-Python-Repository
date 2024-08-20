import os
from os import system
from pathlib import *

route = Path('Proyects\\P6Proyect_KitchenRecipes\\Kitchen Recipes')
amount_recipes = len(list(route.glob('**/*.txt')))
amount_categories = len([r for r in route.iterdir() if route.is_dir()])

print(f'Welcome to the kitchen recipes app. Here you can find {amount_recipes} recipes and {amount_categories} categories.')

def panel_menu():
    while True:
        option = int(input('Select an option below:\n[0] - Exit app\n[1] - Read recipe\n[2] - Create recipe\n[3] - Create category\n[4] - Remove recipe\n[5] - Remove category\n'))
        if option == 0:
            system('cls')
            break
        elif option == 1:
            category = select_category()
            if category != 1:
                recipe = select_recipe(category)
                if recipe != 1:
                    read_recipe(recipe)
        elif option == 2:
            category = select_category()
            if category != 1:
                create_recipe(category)
        elif option == 3:
            create_category()
        elif option == 4:
            category = select_category()
            if category != 1:
                recipe = select_recipe(category)
                if recipe != 1:
                    delete_recipe(recipe)
        elif option == 5:
            category = select_category()
            if category != 1:
                delete_category(category)
        else:
            print('Error, invalid option. Try again')

def select_category():
    categories_list = [r.stem for r in route.iterdir() if route.is_dir()]
    system('cls')
    while True:
        option = int(input(f'Select category below:\n[0] - Back\n{'\n'.join([f'[{categories_list.index(r)+1}] - {r}' for r in categories_list])}\n'))
        if option == 0:
            system('cls')
            return 1
        elif option in range(1,len(categories_list) + 1):
            category = Path(f'{route}\\{categories_list[option-1]}')
            return category
        else:
            print('Error, invalid option. Try again')

def select_recipe(category):    
    system('cls')
    recipes_list = list(category.glob('**/*'))
    option = int(input(f'Select receipe below:\n[0] - Back\n{'\n'.join([f'[{recipes_list.index(r)+1}] - {r.stem}' for r in recipes_list])}\n'))
    while True:
        if option == 0:
            system('cls')
            return 1
        elif option in range(1,len(recipes_list)+1):
            recipe = Path(f'{recipes_list[option-1]}')
            return recipe
        else:
            print('Error, invalid option. Try again')

def delete_category(category):
    Path(category).rmdir()
    print(f'Category "{category.stem}" removed')

def delete_recipe(recipe):
    os.remove(recipe)
    print(f'Recipe "{recipe.stem}" removed')

def create_recipe(category):
    recipe_name = input('Write the recipe title: ') + '.txt'
    recipe_content = input('Write the recipe content: ')
    new_recipe = Path(f'{category}\\{recipe_name}')
    if not os.path.exists(new_recipe):
        Path.write_text(new_recipe,recipe_content)
        print(f'{recipe_name} recipe created')
    else:
        print('A recipe with that name already exist in this category')
    
def create_category():
    category_name = input('Write the category name: ')
    new_category = Path(f'{route}\\{category_name}')
    if not os.path.exists(new_category):
        Path.mkdir(new_category)
    else:
        print('A category with that name already exist')

def read_recipe(recipe):
    system('cls')
    print(recipe.stem)
    print(recipe.read_text())
    input('Press enter to continue:\n')
    system('cls')

panel_menu()