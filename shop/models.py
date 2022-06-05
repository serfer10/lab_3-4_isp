from django.db import models
from PIL import Image

# Create your models here.


class Product(models.Model):
    ACTION = 'action'
    SHOOTER = 'shooter'
    PUZZLE = 'puzzle'
    ADVENTURE = 'adventure'
    INDI = 'indi'
    HORROR = 'horror'

    CHOICE_GROUP = {
        (ACTION, 'action'),
        (SHOOTER, 'shooter'),
        (PUZZLE, 'puzzle'),
        (ADVENTURE, 'adventure'),
        (INDI, 'indi'),
        (HORROR, 'horror'),
    }

    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="product_image", default="product_image/no_image.jpg")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    group = models.CharField(max_length=50, choices=CHOICE_GROUP,default=ACTION)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name