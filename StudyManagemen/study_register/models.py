from django.db import models

# Create your models here.


class Study(models.Model):
    studyid=models.AutoField(primary_key=True)
    studyname=models.CharField(max_length=100)
    studyphase=models.CharField(max_length=100)
    studydescription=models.CharField(max_length=100)
    sponsorname=models.CharField(max_length=100)