from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.


def test(request):
    return HttpResponse("Funciona correctamente")

# creación y borrado de datos


def create(request):
    comment = Comment(name='juanjo', score='5',
                      comment='este es un comentario')
    comment.save()
    return HttpResponse("ruta para creación de modelos")


def delete(request):
    comment = Comment.objects.get(id=1)
    comment.delete()
    return HttpResponse("Ruta para probar los borrados")
