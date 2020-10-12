from django.db import models

# any change to models.py run:
# manage.py makemigrations
# manage.py migrate

class Room(models.Model):
    name        = models.TextField()
    description = models.TextField()
    width       = models.IntegerField()
    length      = models.IntegerField()