from django.db import models


class val(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()
    email = models.EmailField(max_length=200)
