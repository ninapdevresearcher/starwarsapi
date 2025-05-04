from django.http import HttpResponse
import json


def replay_error(text, code):
    data = {
        "success": False,
        "message": text,
        "code": code,
    }
    response = HttpResponse(json.dumps(data), content_type='application/json', status=code)
    return response


def page_not_found(request, exception):
    return replay_error("В нашей вселенной нет такой страницы.", 404)