from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_relation = models.BooleanField('is relation', default=False)
    is_operational = models.BooleanField('is operational', default=False)
    is_customer = models.BooleanField('is customer', default=False)
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.username
