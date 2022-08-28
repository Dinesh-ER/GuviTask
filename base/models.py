from djongo import models


class Users(models.Model):
    email = models.EmailField(max_length=200, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=30, blank=False)
    dob = models.CharField(max_length=12, blank=False)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=30, blank=False)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        db_table = "users"
