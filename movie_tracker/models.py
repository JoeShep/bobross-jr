from django.db import models


class Movie(models.Model):
  title = models.CharField(max_length=100)
  year_released = models.CharField(max_length=4)

  def __str__(self):
    return self.title
