from django.db import models

# Create your models here.


class ProductInfo(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.title + " " + self.price + " " + self.description
