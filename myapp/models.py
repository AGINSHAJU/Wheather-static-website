from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobilenumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
