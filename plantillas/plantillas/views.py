from django.shortcuts import render


def simple(request):
    return render(request, "simple.html", {})


def dinamico(request, nombre):
    categories = ["code","desing","math","bussines"]
    context = {"nombre": nombre, "categories":categories}
    return render(request, "dinamico.html", context)
