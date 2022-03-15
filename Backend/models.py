from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FileType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Prefix(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Prefix"
        verbose_name_plural = "Prefixes"

class Cast(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rating(models.Model):
    rate = models.CharField(max_length=100)

    def __str__(self):
        return "Rating: " + self.name

class Comments(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    comment_file = models.CharField(max_length=100)
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Author: " + self.name +  "File: " + self.comment_file + " Comment: " + self.comment 

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

class File(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    imageArt = CloudinaryField('image') 
    releaseDate = models.CharField(max_length=200)
    downloadable = models.FileField(upload_to="media")
    fileType = models.ForeignKey(FileType, on_delete=models.CASCADE)
    prefix = models.ForeignKey(Prefix, on_delete=models.CASCADE)
    onDisplay = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="Description")
    artiste = models.CharField(max_length=200, blank=True, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, blank=True, null=True)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self):
        return "File Type: " + str(self.fileType.name) + "   |   Title: " + self.title + "   |   Date Uploaded: " + str(self.date_uploaded)