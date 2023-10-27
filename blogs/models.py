from django.db import models

# Create your models here.
class Registration(models.Model):
    yourname = models.CharField(max_length=50)
    username = models.CharField(max_length=100,primary_key=True )
    password = models.CharField(max_length=14)


    class Meta:
        db_table = "registration"


class Join(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=14)


    class Meta:
        db_table = "login_info"

class Blogs(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        db_table = "add_blogs"