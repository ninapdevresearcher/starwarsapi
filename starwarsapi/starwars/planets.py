import json
from django.http import HttpResponse
from starwars.views import SHOW_LIMIT, page_not_found
from itertools import count


class Planet:
    iterator = count(start=1)

    def __init__(self, name: str, rotation_period: int, orbital_period: int, diameter: int, climate: str, gravity: str, terrain: str, surface_water: int, population: int):
        self.name = name
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.residents = []
        self.id = next(self.iterator)
        self.slug = self.name.replace(' ', '-').lower()
        self.url = [f"http://127.0.0.1:8000/character/{self.id}",
                    f"http://127.0.0.1:8000/character/{self.slug}"
        ]

    def to_json(self):
        return self.__dict__


list_of_planets = [Planet("Tatooine", 23, 304, 10465, "arid", "1 standard", "desert", 1, 200000),
                   Planet("Alderaan", 24, 364, 12500, "temperate", "1 standard", "grasslands, mountains", 40, 2000000000),
                   Planet("Yavin IV", 24, 4818, 10200, "temperate, tropical", "1 standard", "jungle, rainforests", 8, 1000),
                   Planet("Hoth", 23, 549, 7200, "frozen", "1.1 standard", "tundra, ice caves, mountain ranges", 100, "unknown"),
                   Planet("Dagobah", 23, 341, 8900, "murky", "unknown", "swamp, jungles", 8, "unknown"),
                   Planet("Bespin", 12, 5110, 118000, "temperate", "1.5 (surface), 1 standard (Cloud City)", "gas giant", 0, 6000000),
                   Planet("Endor", 18, 402, 4900, "temperate", "0.85 standard", "forests, mountains, lakes", 8, 30000000),
                   Planet("Naboo", 26, 312, 12120, "temperate", "1 standard", "grassy hills, swamps, forests, mountains", 12, 4500000000),
                   Planet("Coruscant", 24, 368, 12240, "temperate", "1 standard", "cityscape, mountains", "unknown", 1000000000000),
                   Planet("Kamino", 27, 463, 19720, "temperate", "1 standard", "ocean", 100, 1000000000),
]


def list_planets(request):
    list_of_planets.sort(key=lambda x: x.name)
    part = list_of_planets[:SHOW_LIMIT]
    data = {
        "success": True,
        "total_quantity": len(list_of_planets),
        "data": [pl.to_json() for pl in part],
    }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=201)
    return response


def planet_by_id(request, id_planet):
    try:
        obj = list(filter(lambda x: x.id == id_planet, list_of_planets))[0]
    except Exception as e:
        print(e)
        return page_not_found(request, e)
    else:
        data = {
            "success": True,
            "data": [obj.to_json()],
        }
        response = HttpResponse(json.dumps(data), content_type='application/json', status=201)
        return response


def planet_by_slug(request, slug_planet):
    try:
        obj = list(filter(lambda x: x.slug == slug_planet, list_of_planets))[0]
    except Exception as e:
        print(e)
        return page_not_found(request, e)
    else:
        data = {
            "success": True,
            "data": [obj.to_json()],
        }
        response = HttpResponse(json.dumps(data), content_type='application/json', status=201)
        return response

