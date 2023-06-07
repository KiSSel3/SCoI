from django.db import models
from django.urls import reverse

class Device(models.Model):

    # класс для типа товара, ноутбук, планшет, телефон, пк, наушники, и для них виды услуг из Issue
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='device/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name



class Issue(models.Model):

    # класс для услу к примеру чистка от пыли, замена термопасты, ремонт, замена экрана и т.д
    issue_type = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    device_type = models.ForeignKey(Device, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('services:detail', args=[str(self.id)])
    def __str__(self):
        return self.issue_type



class Client(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField()

    email = models.EmailField()

    phone_number = models.CharField(max_length=50,)

    def __str__(self):
        return self.email
