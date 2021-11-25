from django.db import models

# Create your models here.
class School(models.Model):
    name = models.TextField(verbose_name='学校名',max_length=30)
    created_at = models.DateTimeField(verbose_name='登録日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'School'


class Class(models.Model):
    school = models.ForeignKey(School,verbose_name='学校',default=0,on_delete=models.PROTECT)
    grade = models.IntegerField(verbose_name='学年')
    name = models.CharField(verbose_name='クラス名',max_length=10)

    class Meta:
        verbose_name_plural = 'Class'