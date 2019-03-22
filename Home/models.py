from django.db import models

class User(models.Models):
    userName = models.CharField(max_length=100)
    userDisc = models.TextField(max_length=300)

    def __str__(self):
        return self.userName
    
class Project(models.Model):
    projectName = models.CharField(max_lenth=100)
    projectDisc = models.TextField(max_length=300)

    def __str__(self):
        return self.projectName
        
    
# Create your models here.
