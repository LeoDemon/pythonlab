from __future__ import unicode_literals

from django.db import models

# Create your models here.

#book_info
class book_info(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_purchase_time = models.DateField()

#user_info
class user_info(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_pwd = models.CharField(max_length=100)
    user_type = models.IntegerField()
    user_alias = models.CharField(max_length=100)

