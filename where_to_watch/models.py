from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self):
        return f'Title: {self.title}'

class Service(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length = 200)

    def __str__(self):
        return f'Service: {self.title}'

