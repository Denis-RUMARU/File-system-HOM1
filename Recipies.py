cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ],
    'Паста Карбонара': [
        {'ingredient_name': 'Спагетти', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Бекон', 'quantity': 150, 'measure': 'г'},
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Пармезан', 'quantity': 50, 'measure': 'г'}
    ],
    'Салат Цезарь': [
        {'ingredient_name': 'Куриное филе', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Ромэн салат', 'quantity': 150, 'measure': 'г'},
        {'ingredient_name': 'Пармезан', 'quantity': 50, 'measure': 'г'},
        {'ingredient_name': 'Гренки', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Цезарь соус', 'quantity': 50, 'measure': 'мл'},
        {'ingredient_name': 'Яйцо', 'quantity': 1, 'measure': 'шт'}
    ],
    'Чизкейк Нью-Йорк': [
        {'ingredient_name': 'Сливочный сыр', 'quantity': 500, 'measure': 'г'},
        {'ingredient_name': 'Сахар', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Сметана', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Яйцо', 'quantity': 3, 'measure': 'шт'},
        {'ingredient_name': 'Ванильный экстракт', 'quantity': 1, 'measure': 'ч.л'},
        {'ingredient_name': 'Песочное печенье', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Масло сливочное', 'quantity': 100, 'measure': 'г'},
        {'ingredient_name': 'Лимонный сок', 'quantity': 1, 'measure': 'ст.л'}
    ],
    'Борщ': [
        {'ingredient_name': 'Свекла', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Картофель', 'quantity': 3, 'measure': 'шт'},
        {'ingredient_name': 'Морковь', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Лук', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Капуста', 'quantity': 300, 'measure': 'г'},
        {'ingredient_name': 'Помидоры', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Чеснок', 'quantity': 2, 'measure': 'зубч'},
        {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
        {'ingredient_name': 'Томатная паста', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Лавровый лист', 'quantity': 2, 'measure': 'шт'}
    ],
    'Рататуй': [
        {'ingredient_name': 'Баклажан', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Цукини', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Помидор', 'quantity': 4, 'measure': 'шт'},
        {'ingredient_name': 'Перец сладкий', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Лук', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Чеснок', 'quantity': 2, 'measure': 'зубч'},
        {'ingredient_name': 'Оливковое масло', 'quantity': 3, 'measure': 'ст.л'}
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

result = get_shop_list_by_dishes(['Чизкейк Нью-Йорк', 'Рататуй'], 2)
print(result)
