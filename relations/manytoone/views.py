from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.


def create(request):
    reporter = Reporter(first_name='juanjo',
                        last_name='ruiz', email='juanco@demo.com')
    reporter.save()

    art1 = Article(headline='Lorem_ipsum_dolot',
                   pub_date=date(2022, 5, 5), reporter=reporter)
    art2 = Article(headline='Lorem_set_imet',
                   pub_date=date(2022, 3, 7), reporter=reporter)
    art3 = Article(headline='Lorem_aimet_lorem',
                   pub_date=date(2022, 4, 9), reporter=reporter)

    art1.save()
    art2.save()
    art3.save()

    result = art1.reporter.first_name
    # busqueda de elementos relacionados desde entidad u objeto que no tiene un elemento del otro en su modelo.
    # de esta forma se pueden realizar todas las consultas vistas, tanto genéricas como de ordenación
    consult = reporter.article_set.all()
    consult1 = reporter.article_set.filter(headline='Lorem_ipsum_dolot')
    count = reporter.article_set.count()
    
    return HttpResponse(count)
