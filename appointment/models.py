from django.db import models

# Create your models here.
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=30, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    name = models.TextField(max_length=30, default='')
    mon = models.TextField(default='')
    tue = models.TextField(default='')
    wed = models.TextField(default='')
    thr = models.TextField(default='')
    fri = models.TextField(default='')
    sat = models.TextField(default='')
    sun = models.TextField(default='')

    def __str__(self):
        return f'{self.name}'