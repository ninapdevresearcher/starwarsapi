from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index),
    path('characters/', v.list_characters),
    path('planets/', v.list_planets),
    path('vehicles/', v.list_vehicles),
    path('sentient_species/', v.list_sentient_species),
    path('character/<slug:slug_char>', v.character),
]