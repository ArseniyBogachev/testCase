from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class ItemMenu(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('btn', kwargs={'btn': self.url, 'url': self.menu})

# Create your models here.
