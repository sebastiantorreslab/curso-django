from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

#para la relacion many to many se declara solo en una de las dos clases
class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

        #aqui ya hemos modelado nuestros datos para la relación many to many


  