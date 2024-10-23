import json
from django.http import HttpResponse
from starwars.views import SHOW_LIMIT, page_not_found
from itertools import count


class Starship:
    iterator = count(start=1)

    def __init__(self, name: str, model: str, manufacturer: str, cost: int, length: int, speed: int, crew: tuple, passengers: int, cargo_capacity: int, starship_class: str):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost
        self.length = length # meters
        self.max_atmosphering_speed = speed
        self.crew = crew #number or range - tuple
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.starship_class = starship_class
        self.id = next(self.iterator)
        self.slug = self.name.replace(' ', '-').lower()

    def to_json(self):
        return self.__dict__


list_of_starships = [Starship("Star Destroyer", "Imperial I-class Star Destroyer", "Kuat Drive Yards", 150000000, 1600, 975, (47060,), 0, 36000000, "Star Destroyer"),
                      Starship("CR90 corvette", "CR90 corvette", "Corellian Engineering Corporation", 3500000, 150, 950, (30, 165), 600, 3000000, "corvette"),
                      Starship("Sentinel-class landing craft", "Sentinel-class landing craft", "Sienar Fleet Systems, Cyngus Spaceworks", 240000, 38, 1000, (5, ), 75, 180000, "landing craft"),
                      Starship("Death Star", "DS-1 Orbital Battle Station", "Imperial Department of Military Research, Sienar Fleet Systems", 1000000000000, 120000, 0, (342953,), 843342, 1000000000000, "Deep Space Mobile Battlestation"),
                      Starship("Millennium Falcon", "YT-1300 light freighter", "Corellian Engineering Corporation", 100000, 34, 1050, (4, ), 6, 100000, "Light freighter"),
                      Starship("Y-wing", "BTL Y-wing", "Koensayr Manufacturing", 134999, 14, 1000, (2,), 0, 110, "assault starfighter"),
                      Starship("X-wing", "T-65 X-wing", "Incom Corporation", 149999, 12, 1050, (1,), 0, 110, "Starfighter"),
                      Starship("TIE Advanced x1", "Twin Ion Engine Advanced x1", "Sienar Fleet Systems", 0, 9, 1200, (1,), 0, 150, "Starfighter"),
                      Starship("Executor", "Executor-class star dreadnought", "Kuat Drive Yards, Fondor Shipyards", 1143350000, 19000, 0, (279144,), 38000, 250000000, "Star dreadnought"),
                      Starship("Rebel transport", "GR-75 medium transport", "Gallofree Yards, Inc.", 0, 90, 650, (6,), 90, 19000000, "Medium transport")
]


# есть еще параметр pilots, через который можно связать таблицу с characters - подумать


def list_starships(request):
    list_of_starships.sort(key=lambda x: x.name)
    part = list_of_starships[:SHOW_LIMIT]
    data = {
        "success": True,
        "total_quantity": len(list_of_starships),
        "data": [ch.to_json() for ch in part],
    }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=201)
    return response


def starship_by_id(request, id_ship):
    try:
        obj = list(filter(lambda x: x.id == id_ship, list_of_starships))[0]
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


def starship_by_slug(request, slug_ship):
    try:
        obj = list(filter(lambda x: x.slug == slug_ship, list_of_starships))[0]
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