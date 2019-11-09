from django.db import models

# Create your models here.
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    name = models.TextField()
    scheule = models.ArrayField(base_field=models.IntegerField())