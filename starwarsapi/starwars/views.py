from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import json
# from rest_framework.views import exception_handler


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


def character(request, slug_char):
    print(request.GET)
    return HttpResponse(f"Information about character: {slug_char}.")


def list_characters(request):
    return HttpResponse("list_characters")


def list_planets(request):
    return HttpResponse("list_planets")


def list_vehicles(request):
    return HttpResponse("list_vehicles")


def list_sentient_species(request):
    return HttpResponse("list_sentient_species")


# ??????????????????????????????????
# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code
#
#     return response


# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'my_project.my_app.utils.custom_exception_handler'
# }