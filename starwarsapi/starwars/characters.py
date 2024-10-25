import json
from django.http import HttpResponse
from starwars.views import SHOW_LIMIT, page_not_found
from itertools import count


class Character:
    iterator = count(start=1)

    def __init__(self, name: str, age: int, power: int, homeworld: str, side: str):
        self.name = name
        self.age = age
        self.power = power
        self.homeworld = homeworld # planet
        self.side = side # [good, bad, neutral]
        self.id = next(self.iterator)
        self.slug = self.name.replace(' ', '-').lower()
        self.url = [f"http://127.0.0.1:8000/character/{self.id}",
                    f"http://127.0.0.1:8000/character/{self.slug}"
    ]

    def to_json(self):
        return self.__dict__


list_of_characters = [Character("Luck Skywalker", 26, 57, "The Earth", "good"),
                      Character("Darth Sidious", 320, 83, "Hell", "bad"),
                      Character("Yoda", 369, 87, "Green magic world", "good"),
                      Character("Ahsoka Tano", 43, 53, "Shili", "good"),
                      Character("Obi-Wan Kenobi", 86, 67, "Coruscant", "good"),
                      Character("Anakin Skywalker", 58, 75, "The Earth", "bad"),
]


def list_characters(request):
    list_of_characters.sort(key=lambda x: x.name)
    part = list_of_characters[:SHOW_LIMIT]
    data = {
        "success": True,
        "total_quantity": len(list_of_characters),
        "data": [ch.to_json() for ch in part],
    }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
    return response


def character_by_id(request, id_char):
    try:
        obj = list(filter(lambda x: x.id == id_char, list_of_characters))[0]
    except Exception as e:
        print(e)
        return page_not_found(request, e)
    else:
        data = {
            "success": True,
            "data": [obj.to_json()],
        }
        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response


def character_by_slug(request, slug_char):
    try:
        obj = list(filter(lambda x: x.slug == slug_char, list_of_characters))[0]
    except Exception as e:
        print(e)
        return page_not_found(request, e)
    else:
        data = {
            "success": True,
            "data": [obj.to_json()],
        }
        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response


#добавить иконку для персонажа
#сортировка по полю
#добавить поле pilots для связи таблицы кораблей и персонажей - это список