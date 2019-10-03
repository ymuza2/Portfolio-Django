from django.db import models

# Create your models here.
class job(models.Model):
    image = models.ImageField(upload_to='images/') #las imagenes se van a guardar en la carpeta 'images/'
    summary = models.CharField(max_length=200)
