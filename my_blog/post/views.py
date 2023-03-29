from django.shortcuts import render
from .models import Autor, Entry
from django.http import HttpResponse


# Create your views here.

def queries(request):
    # obtener todos los elementos en un objeto
    authors = Autor.objects.all()

    # obtener datos filtrando por condición
    filtered = Autor.objects.filter(email='normanlarry@example.org')

    # obtener un único objeto

    autor = Autor.objects.get(id=1)

    # Utilizando consulta limit

    limit = Autor.objects.all()[:10]

    # Aplicando el offset es decir cuantos valores nos saltamos para empezar a contar
    # obtener 10 elementos saltando los 5 primeros

    offsets = Autor.objects.all()[5:10]

    # Métodos de ordenación order By

    orders = Autor.objects.all().order_by('email')

    # Obtener todos los elementos que su id sean menores o igual a 15
    filtereds2 = Autor.objects.filter(id__lte=15)

    # obtener todos los autores que contienen en su nombre la palabra yes

    filtereds3 = Autor.objects.filter(name__contains="yes")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'autor': autor, 'limit': limit, 'offsets': offsets, 'orders': orders, 'filtereds2': filtereds2, 'filtereds3': filtereds3})

def update(request):
    autor = Autor.objects.get(id=1)
    autor.name = 'juanjo'
    autor.email = 'juanjo@demo.com'
    autor.save()
    return HttpResponse("modificado")
