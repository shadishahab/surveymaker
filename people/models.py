from django.conf import settings
from django.db import models

class Person(models.Model):
    phone_number = models.CharField(max_length=11)
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = 'sender'
        )