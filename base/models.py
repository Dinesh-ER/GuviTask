import os
from djongo import models
from django.conf import settings
from djongo.storage import GridFSStorage


grid_fs_storage = GridFSStorage(collection='photos', base_url=os.path.join(settings.BASE_DIR,'photos/'))

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=30, blank=True)
    dob = models.CharField(max_length=12, blank=True)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="photos", storage=grid_fs_storage)
    
    class Meta:
        db_table = "users"
