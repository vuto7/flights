from django.db import models
from django.contrib.auth.models import User  

class Identity(models.Model):
    GENDERS=(("Female","Female"),("Male","Male"))
    STATUSES=(("Verified","Verified"),("Registered","Registered"),("Unverified","Unverified"))

    nrcid = models.CharField(max_length=12)
    status = models.CharField(choices=STATUSES, max_length=10)
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDERS, max_length=10)
    dateofbirth = models.DateField(max_length=10)
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=70)


class Employee(models.Model):
    employeeNo = models.CharField(max_length=15)
    aeNo = models.CharField(max_length=15)
    lineMinistry = models.CharField(max_length=30)
    institution = models.CharField(max_length=50)
    institutionAcronymn = models.CharField(max_length=6)
    station = models.CharField(max_length=15)
    identity = models.OneToOneField(Identity, on_delete=models.CASCADE)
    

class TimeStamp(models.Model):
    timeStampNo = models.CharField(max_length=15)
    timeVerified = models.DateTimeField(max_length=55)
    isVerified = models.CharField(max_length=15)
    location = models.CharField(max_length=15) 
    employeeNo = models.OneToOneField(Employee, on_delete=models.CASCADE)
    userVerifiedBy = models.OneToOneField(User, related_name='verificationUser', null=True, on_delete=models.SET_NULL)
    
    



    