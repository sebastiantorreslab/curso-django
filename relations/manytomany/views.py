from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article
from datetime import date

# Create your views here.


def create(request):
    # primero debemos crear y guardar los elementos y objetos para poder relacionarlos despues
    art1 = Article(headline="Articulo primero")
    art2 = Article(headline="Articulo segundo")
    art3 = Article(headline="Articulo tercero")

    pub1 = Publication(title="publicación primera")
    pub2 = Publication(title="publicación segunda")
    pub3 = Publication(title="publicación tercera")
    pub4 = Publication(title="publicación cuarta")
    pub5 = Publication(title="publicación quinta")
    pub6 = Publication(title="publicación sexta")
    pub7 = Publication(title="publicación septima")

    pub1.save()
    pub2.save()
    pub3.save()
    pub4.save()
    pub5.save()
    pub6.save()
    pub7.save()

    art1.save()
    art2.save()
    art3.save()

    # una vez creados y guardados ahora si los podremos relacionar
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    # pub1 = Publication.objects.get(id=1)
    #result = art1.articles_set.all() --> así puedo realizar la consulta desde la otra entidad relacionada
    # de este mismo modo se podría hacer desde publicaciones asignadole artículos por el método add.

    result = art1.publications.all()

    #art1.publications.remove(pub1) así podemos eliminar una relación

    return HttpResponse(result)
