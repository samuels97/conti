from django.db import models

# Create your models here.
class PContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.CharField(max_length=200)
    date_written = models.DateField()

    def __str__():
        return self.name

class AdminPost(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    Poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    public = models.Boolean()

    def __str__(self):
        return self.headline
