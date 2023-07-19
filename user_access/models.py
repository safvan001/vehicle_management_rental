from django.db import models
from django.contrib.auth.models import User


#AbstractUser model for customized user model
from django.contrib.auth.models import AbstractUser

class User1(AbstractUser):
    ROLES=[
        ('Super admin', 'Super admin'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    user_type=models.CharField(max_length=20,choices=ROLES)

    def __str__(self):
        return self.user_type

class UserAccess(models.Model):

    user = models.OneToOneField(User1, on_delete=models.CASCADE, related_name='user_access')
    can_edit = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)

    def __str__(self):
         return str(self.user)


# vehicle management's model
class Vehicle(models.Model):
    # One-to-one relationship with User1
    vehicle = models.OneToOneField(User1, on_delete=models.CASCADE, related_name='vehicle')



    VEHICLE_TYPES = (
        ('Two', 'Two wheelers'),
        ('Three', 'Three wheelers'),
        ('Four', 'Four wheelers'),
    )
    vehicle_number=models.CharField(max_length=25,unique=True, blank=False, null=False)
    vehicle_type=models.CharField(max_length=50,choices=VEHICLE_TYPES)
    vehicle_model=models.CharField(max_length=100)
    vehicle_description=models.TextField()



    def __str__(self):
        return self.vehicle_number




