from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def indexw(request):
    return HttpResponse("Hello, world.jjmjm")