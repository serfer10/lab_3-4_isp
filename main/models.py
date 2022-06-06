from django.db import models

# Create your models here.


class Clinets(models.Model):
    name = models.CharField("Name", max_length=50)
    surname = models.CharField("Surname", max_length=50)

    def __str__(self):
        return self.name

    # rename table
    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"


# made that and added to admin.py
