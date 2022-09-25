from django.db import models

# Create your models here.
class front_end(models.Model):
    note_title = models.CharField(max_length=120)
    tag_line = models.CharField(max_length=122)
    note = models.CharField(max_length=100)

