from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_views(request):
    template_name = 'calculator/index.html'
    pages = {
        'Главная страница': reverse('home'),
        'Блюдо 1': reverse('omlet'),
        'Блюдо 2': reverse('pasta'),
        'Блюдо 3': reverse('buter'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def make_omlet(request):
    ingredient_list = list()
    str_for_http_response = str()
    ammount_str = request.GET.get("servings")
    servings = 1
    if ammount_str != None:
        servings = int(ammount_str)

    for ingredient, amount in DATA['omlet'].items():
        ingredient_list.append(ingredient)
        str_for_http_response += f'{ingredient} : {str(amount * servings )} '
    print(request.GET.get("servings"))
    return HttpResponse(str_for_http_response)

def make_pasta(request):
    print(DATA['pasta'])
    ingredient_list = list()
    for ingredient in DATA['pasta'].items():
        print(ingredient)
        ingredient_list.append(ingredient)
    return HttpResponse(ingredient_list)

def make_buter(request):
    print(DATA['buter'])
    ingredient_list = list()
    for ingredient in DATA['buter'].items():
        print(ingredient)
        ingredient_list.append(ingredient)
    return HttpResponse(ingredient_list)
