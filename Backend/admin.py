from django.contrib import admin
from .models import Genre, Rating, Comments, File, Prefix, FileType, Cast

admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comments)
admin.site.register(File)
admin.site.register(Prefix)
admin.site.register(FileType)
admin.site.register(Cast)