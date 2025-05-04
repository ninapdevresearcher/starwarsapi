from django.urls import path, include
from . import views as v
from . import characters as ch
from . import planets as pl
from . import starships as st
from rest_framework.routers import DefaultRouter, SimpleRouter


# router = DefaultRouter()
# router.register('planet', v.GetMethod, basename='planet')
# urlpatterns = router.urls

router = SimpleRouter()
router.register('planet', v.GetMethodPlanet, basename='planet')
router.register('character', v.GetMethodCharacter, basename='character')
router.register('starship', v.GetMethodStarship, basename='starship')


urlpatterns = [
    path('', include(router.urls)),
    path('', v.index),
    path('characters/<int:id_char>', ch.character_by_id),
    path('characters/<slug:slug_char>', ch.character_by_slug),
    path('characters/', ch.list_characters),
    path('planets/<int:id_planet>', pl.planet_by_id),
    path('planets/<slug:slug_planet>', pl.planet_by_slug),
    path('planets/', pl.list_planets),
    path('starships/<int:id_ship>', st.starship_by_id),
    path('starships/<slug:slug_ship>', st.starship_by_slug),
    path('starships/', st.list_starships),
]

