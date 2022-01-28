from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class School(models.Model):
    name = models.TextField(verbose_name='学校名',max_length=30)

    class Meta:
        verbose_name_plural = 'School'

    def __str__(self):
        return self.name


class Class(models.Model):
    class_school = models.ForeignKey(School,verbose_name='学校',default=0,on_delete=models.PROTECT)
    class_name = models.CharField(verbose_name='クラス名',max_length=10)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Class'

    def __str__(self):
        return self.class_name


class CustomUser(AbstractUser):
    SELECTION = (
        ('1','admin'),
        ('2','teacher'),
        ('3','student'),
    )

    user_school = models.ForeignKey(School,verbose_name='学校',null=True,blank=True,on_delete=models.PROTECT)
    user_class = models.ForeignKey(Class,verbose_name='クラス',null=True,blank=True,on_delete=models.PROTECT)
    user_grade = models.IntegerField(verbose_name='学年',null=True,blank=True)
    user_auth = models.CharField(verbose_name='権限',choices=SELECTION,max_length=1)

    class Meta:
        verbose_name_plural = 'CustomUser'
