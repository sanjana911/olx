from django.db import models

# Create your models here.

#vehicle(name,number,year,fuel_type,owner_type,running_km,accident_history,price,year,phone,is_active,created_at)


class Vehicle(models.Model):

    name = models.CharField(max_length=200)

    number = models.CharField(max_length=15)

    FUEL_TYPE_CHOICES=(
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("cng","cng"),
        ("ev","ev")
    )

    fuel_type = models.CharField(max_length=200,choices=FUEL_TYPE_CHOICES)

    OWNER_TYPE_CHOICES=(
        ("single","single"),
        ("second","second"),
        ("third","third"),
        ("other","other"),
    )

    owner_type = models.CharField(max_length=200,choices=OWNER_TYPE_CHOICES)

    running_km = models.DecimalField(max_digits=8,decimal_places=2)

    accident_history = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=8,decimal_places=2)

    year = models.CharField(max_length=20)

    phone = models.CharField(max_length=20)

    is_active = models.BooleanField(default= True)

    created_at = models.DateTimeField(auto_now_add=True)