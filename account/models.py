from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    image = models.ImageField(upload_to='profiles/img', blank=True, null=True)

    def __str__(self):
        return self.user.username