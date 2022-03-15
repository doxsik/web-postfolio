from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()
    description = models.CharField(max_length=248)
    textar = models.TextField(default='')

    def __str__(self):
        return self.title
