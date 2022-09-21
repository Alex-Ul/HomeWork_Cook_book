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
print(f"\nTask 2\n")

def get_shop_list_by_dishes(menu, person_count):
    shop_list_by_dishes = {}
    shop_list = {}
    for dish_d in menu:
        recipe = list(cook_book[dish_d])
        for item in recipe:
            ingredient_n, quantity, measure = item.values()
            item.pop('ingredient_name')
            if ingredient_n in shop_list_by_dishes.keys():
                same_ing = shop_list_by_dishes[ingredient_n]
                item['quantity'] = person_count * int(item.get('quantity')) + int(same_ing.get('quantity'))
            else:
                item['quantity'] = person_count * int(item.get('quantity'))
            shop_list[ingredient_n] = item
            shop_list_by_dishes.update(shop_list)
    print(f"Список для поупок: \n{shop_list_by_dishes}")


dishes = []
menu = list(cook_book.keys())
print('Выберите блюдо для покупки ингридиентов:')
for dish in menu:
    print(dish)
    q1 = input('Хотите добавить блюдо? - да/нет ')
    if q1 == 'да':
        dishes.append(dish)
number_per = int(input('Введите количество персон: '))
print(f"Ваш выбор:\nблюда - {dishes}\nколичество персон - {number_per}")

get_shop_list_by_dishes(dishes, number_per)
