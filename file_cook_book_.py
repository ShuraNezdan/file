def open_file_add_dict(name_file):
    """ Задача 1. Функция читает файл и переводит его в словарь."""
    
    ingredients = []
    cook_book = {}
    control = 1

    with open('recipes.txt') as file:
        for line in file:
            # Проверяем название блюда, создаем ключ в словаре
            if line.strip() != "" and control == 1:
                dish = line.strip()
                cook_book[dish] = []
                control = 2
            # проходим строку с колличеством ингридиентов
            elif line.strip() != "" and control == 2:
                control = 3
            # Делим строку с ингридиентами на список, присваиваем словарю значения из списка
            elif line.strip() != "" and control == 3:
                food_list = line.strip().split(' | ')
                ingredients_elements = {'ingredient_name': food_list[0], 'quantity': food_list[1], 'measure': food_list[2]}
                ingredients.append(ingredients_elements)
                cook_book[dish] = ingredients
            # Когда деление между блюдами в файле (пустая строка), обнуляем игридиенты для следющего блюда, 
            # переводим контрол в 1 чтобы далее читало название блюда
            elif line.strip() == "":
                ingredients = []
                control = 1
    
    return cook_book

def print_cook_book():
    # Просто печать на экран для контроля словаря cook_book
    c = open_file_add_dict('recipes.txt')
    for key, value in c.items():
        print()
        print(key)
        for i in value:
            print(i)
 
def get_shop_list_by_dishes(dishes, person_count):
    """
    Задача 2. Функция которая принимает названия блюд и колличество человек.
    Выдает новый словарь с необходимыми покупками.
    """

    cook_book = open_file_add_dict('recipes.txt')
    shopping_list = {}
    
    # Перебераем вводимые блюда
    for dish in dishes:
        
        # Перебераем блюда из словаря-файла
        for key, values in cook_book.items():
            
            # Проверяем на идеинтичность
            if dish == key:
                
                # Перечисляем ингридиенты
                for value in values:
                    list_ingredients = {'measure': '', 'quantity': 0}    # Обнуляем list_ingredients
                    list_ingredients['measure'] = value['measure']
                    
                    # Перемножаем ингридиент на колличество человек 
                    list_ingredients['quantity'] = int(value['quantity']) * person_count

                    # Проверяем на повтор в ранее созданом словаре shopping_list
                    # Если  нет, проходим мимо, если есть складываем.
                    if value['ingredient_name'] in shopping_list:
                        list_ingredients['quantity'] = shopping_list[value['ingredient_name']]['quantity'] + list_ingredients['quantity']
                        shopping_list[value['ingredient_name']] = list_ingredients
                    else:
                        shopping_list[value['ingredient_name']] = list_ingredients
    return shopping_list

def print_get_shop_list_by_dishes(dishes, person_count):
    # Просто печать на экран для контроля всловаря покупок
    dict_print = get_shop_list_by_dishes(dishes, person_count)
    for key, values in dict_print.items():
        print()
        print(key)
        for key_2 in values:
            print(f'{values[key_2]}')

#Печать и проверка задачи номер 1.
# print_cook_book()

#Печать и проверка задачи номер 2.
print_get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Курица в сливках'], 1)