from django.db import models

# Create your models here.
class PContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.CharField(max_length=200, default="Nothing here")
    date_written = models.DateField()

    def __str__(self):
        return self.name

class AdminPost(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.headline
