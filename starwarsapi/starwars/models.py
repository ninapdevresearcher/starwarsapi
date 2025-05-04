from datetime import datetime
from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    orbital_period = models.IntegerField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    climate = models.CharField(max_length=255, null=True, blank=True)
    gravity = models.CharField(max_length=255, null=True, blank=True)
    terrain = models.CharField(max_length=255, null=True, blank=True)
    surface_water = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True) #default=datetime.now(), blank=True)
    time_update = models.DateTimeField(auto_now=True) #default=datetime.now(), blank=True)


class Character(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    mass = models.IntegerField(null=True, blank=True)
    hair_color = models.CharField(max_length=100, null=True, blank=True)
    eye_color = models.CharField(max_length=100, null=True, blank=True)
    birth_year = models.CharField(max_length=100, null=True, blank=True)

    homeworld = models.ForeignKey('Planet', on_delete=models.PROTECT, related_name="home")
    starships = models.ManyToManyField("Starship", blank=True, related_name='pilots')

    time_create = models.DateTimeField(auto_now_add=True) #default=datetime.now(), blank=True)
    time_update = models.DateTimeField(auto_now=True) #default=datetime.now(), blank=True)


class Starship(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    crew = models.IntegerField(null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)
    cargo_capacity = models.IntegerField(null=True, blank=True)
    starship_class = models.IntegerField(null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True) #default=datetime.now(), blank=True)