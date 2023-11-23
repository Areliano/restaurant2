from django.db import models

# Create your models here.

#class Homepage(models.Model):
#    heading = models.CharField(max_length=500)
 #   btn = models.CharField(max_length=20)
  #  image = models.ImageField(upload_to='homepage', default='homepage.jpg')

   # def __str__(self):
    #    return self.heading

class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    person = models.IntegerField()
