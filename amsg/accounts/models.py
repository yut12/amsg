from django.db import models
from django.contrib.auth.models import AbstractUser
from task.models import School

# Create your models here.


class CustomUser(AbstractUser):
    school = models.ForeignKey(
        School, verbose_name='学校', default=0, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'CustomUser'


fdxhxh
<<<<<<< HEAD
ygvygbuhbuhub
fucker
=======
>>>>>>> 9777d766073e6772abd53f2515459f8274399274
