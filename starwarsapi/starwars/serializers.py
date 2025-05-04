from rest_framework import serializers
from .models import*


class PlanetSerializer(serializers.ModelSerializer):
    class Meta():
        model = Planet
        fields = "__all__"


class CharacterSerializer(serializers.ModelSerializer):
    class Meta():
        model = Character
        fields = "__all__"


class StarshipSerializer(serializers.ModelSerializer):
    class Meta():
        model = Starship
        fields = "__all__"