from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to="photos/")
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
