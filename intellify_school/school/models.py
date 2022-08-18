from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    hod_name = models.CharField(max_length=100, default="Enter HOD Name here")
    students_no = models.CharField(max_length=100, default="Enter no. of students here")
    phone = models.CharField(max_length=100, default="Enter Phone no. here")
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)