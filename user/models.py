from django.db import models


# Create your models here.
class UserModel(models.Model):
    # class Meta:
    #     db_table = 'user'

    name = models.CharField(max_length=255)
    age = models.IntegerField()
