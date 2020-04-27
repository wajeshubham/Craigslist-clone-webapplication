from django.db import models


# Create your models here.
class Search(models.Model):
    searches = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.searches}'
