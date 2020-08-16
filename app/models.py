from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    mobile_no = models.CharField(max_length=14)
    email = models.EmailField()
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name