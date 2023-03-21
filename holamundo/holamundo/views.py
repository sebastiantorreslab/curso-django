from django.http import HttpResponse


def saludo(request):
    return HttpResponse("holamundo")


def despedida(request):
    return HttpResponse("despedida")


def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("eres mayor de edad")
    else:
        return HttpResponse("no eres mayor de edad")
