print(f"Task 1\n")

cook_book = {}

with open('recipes.txt', 'r', encoding='utf8') as recipes_list:
    for line in recipes_list:
        dish = []
        dish_rec = {}
        dish_name = line.strip()
        ingredients_number = recipes_list.readline()
        for i in range(int(ingredients_number)):
            ing = recipes_list.readline()
            ingredient_name, ingredients_number, measure = ing.split(' | ')
            ingredient = {'ingredient_name': ingredient_name, 'quantity': ingredients_number,
                          'measure': measure.strip()}
            dish.append(ingredient)
        dish_rec[dish_name] = dish
        cook_book.update(dish_rec)
        recipes_list.readline()
print(cook_book)
