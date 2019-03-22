from django.db import models


# Create your models here.


class User(models.Model):
    
    userName = models.CharField(max_length=100)
    userDisc = models.TextField(max_length=300)
    bakraField = models.CharField(max_length=20)

    def __str__(self):
        return self.userName


class Project(models.Model):
    #question = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    projectDisc = models.TextField(max_length=300)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.projectName

    # def delete(self, *args, **kwargs):
    #     self.pdf.delete()
    #     self.cover.delete()
    #     super().delete(*args, **kwargs)
