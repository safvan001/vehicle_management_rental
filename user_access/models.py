# user_access/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User1(AbstractUser):
    ROLES = [
        ('Super admin', 'Super admin'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    user_type = models.CharField(max_length=20, choices=ROLES)
    user_access = models.OneToOneField('UserAccess', related_name='user11', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user_type

class UserAccess(models.Model):
    user = models.OneToOneField(User1, related_name='access', on_delete=models.CASCADE, null=True, blank=True)
    can_edit = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


# vehicle management's model
class Vehicle(models.Model):
    # ForeignKey relationship with User1
    vehicle = models.ForeignKey(User1, on_delete=models.CASCADE, related_name='vehicles')

    VEHICLE_TYPES = (
        ('Two', 'Two wheelers'),
        ('Three', 'Three wheelers'),
        ('Four', 'Four wheelers'),
    )

    vehicle_number = models.CharField(max_length=25, unique=True, blank=False, null=False)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
