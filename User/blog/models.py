from django.db import models


class User(models.Model):
    """A model of a rock band."""
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    is_admin = models.BooleanField(default=False)
