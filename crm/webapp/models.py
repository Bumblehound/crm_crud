from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=200)
    country = models.CharField(max_length=20)

    def __str__(self):
        return F"{self.first_name.strip()} {self.last_name.strip()}"