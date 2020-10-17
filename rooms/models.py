from django.db import models

# any change to models.py run:
# manage.py makemigrations
# manage.py migrate

class Room(models.Model):
    name            = models.CharField(max_length=50) #charfield requires max_length
    description     = models.TextField(blank=True, null=True)
    wall_texture    = models.CharField(max_length=50)
    floor_texture   = models.CharField(max_length=50)
    width           = models.IntegerField()
    length          = models.IntegerField()