from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import json
# from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .planets import list_of_planets
from .starships import list_of_starships
from .characters import list_of_characters
from .serializers import *


SHOW_LIMIT = 5


def fill_out_the_json(code, data_list):
    error_list = {404: "В нашей вселенной нет такой страницы."}
    if code == 200:
        return {
            "success": True,
            "message": text,
            "data": {},
        }
    code = code if code in error_list else 404
    text = error_list.get(code, 404)
    return {
        "success": False,
        "message": text,
        "error_code": code,
        "data": {}
    }

#415 Unsupported Media Type
#500 Internal Server Error
#501 Not Implemented
#Возвращается, если текущий метод неприменим (не реализован) к объекту запроса.


#array with errors, not just error code
# { "errors": [{
#   "status": "422",
#   "title": "Title already exist",
# }]}

# гипермедиа
#"links": { "self": "http://localhost/articles/1" },


def index(request):
    data = {
            "success": True,
            "message": "Hello Star Wars",
            "data": {},
        }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=201)
    return response


def page_not_found(request, exception):
    return replay_error("В нашей вселенной нет такой страницы.", 404)


def replay_error(text, code):
    data = {
        "success": False,
        "message": text,
        "code": code,
    }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=code)
    return response


class GetMethodPlanet(viewsets.ModelViewSet):
    model_name = Planet
    queryset = model_name.objects.all()
    serializer_class = PlanetSerializer

    def list(self, request, *args, **kwargs):
        # data = list(Planet.objects.all().values())
        list_of_planets.sort(key=lambda x: x.name)
        objs = [pl.to_json() for pl in list_of_planets]
        data = objs[:5]
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(self.model_name.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        model_serializer_data = self.serializer_class(data=request.data)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Added Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        model_data = self.model_name.objects.filter(id=kwargs['pk'])
        if model_data:
            model_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        model_details = self.model_name.objects.get(id=kwargs['pk'])
        model_serializer_data = PlanetSerializer(model_details, data=request.data, partial=True)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data Not found", "status": status_code})


class GetMethodCharacter(viewsets.ModelViewSet):
    model_name = Character
    queryset = model_name.objects.all()
    serializer_class = CharacterSerializer

    def list(self, request, *args, **kwargs):
        # data = list(Planet.objects.all().values())
        list_of_planets.sort(key=lambda x: x.name)
        objs = [pl.to_json() for pl in list_of_planets]
        data = objs[:5]
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(self.model_name.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        model_serializer_data = self.serializer_class(data=request.data)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Added Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        model_data = self.model_name.objects.filter(id=kwargs['pk'])
        if model_data:
            model_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        model_details = self.model_name.objects.get(id=kwargs['pk'])
        model_serializer_data = PlanetSerializer(model_details, data=request.data, partial=True)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data Not found", "status": status_code})


class GetMethodStarship(viewsets.ModelViewSet):
    model_name = Starship
    queryset = model_name.objects.all()
    serializer_class = StarshipSerializer

    def list(self, request, *args, **kwargs):
        # data = list(Planet.objects.all().values())
        list_of_planets.sort(key=lambda x: x.name)
        objs = [pl.to_json() for pl in list_of_planets]
        data = objs[:5]
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(self.model_name.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        model_serializer_data = self.serializer_class(data=request.data)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Added Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        model_data = self.model_name.objects.filter(id=kwargs['pk'])
        if model_data:
            model_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        model_details = self.model_name.objects.get(id=kwargs['pk'])
        model_serializer_data = PlanetSerializer(model_details, data=request.data, partial=True)
        if model_serializer_data.is_valid():
            model_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data Not found", "status": status_code})