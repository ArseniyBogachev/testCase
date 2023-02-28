from django.db import models


class Menu(models.Model):
    url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.url


class ParentMenu(models.Model):
    name = models.CharField(max_length=20)
    children = models.ForeignKey(Menu, on_delete=models.CASCADE)
    url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

#
# class ChildrenMenu(models.Model):
#     name = models.CharField(max_length=20)

# Create your models here.
