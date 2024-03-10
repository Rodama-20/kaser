from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to="photos/")
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
