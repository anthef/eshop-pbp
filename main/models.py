from django.db import models

#model for product entry
class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
