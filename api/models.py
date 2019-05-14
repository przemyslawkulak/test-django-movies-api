from django.db import models


class Director(models.Model):
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=256, default='')
    year = models.IntegerField()
    length = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='images', blank=True)
    director = models.OneToOneField(Director, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
