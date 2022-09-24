from django.db import models

# Create your models here.
class email(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=15)
    subject = models.CharField(max_length=15)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 
