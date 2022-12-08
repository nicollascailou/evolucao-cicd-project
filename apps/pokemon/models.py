from django.db import models

# Create your models here.


class Pokemon(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    weight = models.BigIntegerField()
    height = models.BigIntegerField()
    base_experience = models.BigIntegerField()



