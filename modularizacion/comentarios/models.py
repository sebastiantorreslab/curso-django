from django.db import models

# Create your models here.
class Comment(models.Model):

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, null=False,default="Firma"
    )

    def __str__(self):
        return self.name  
        
 # siempre es recomendable realizar la definición del str
# de esta manera vamos a ir creando cada uno de los modelos que necesitamos en nuestra aplicación
# cada vez que realicemos una modificación en cualquier archivo de modelos tenemos que migrar nuevamaente los datos


