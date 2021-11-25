from django.db import models

# Create your models here.
class School(models.Model):
    name = models.TextField(verbose_name='学校名',max_length=30)
    created_at = models.DateTimeField(verbose_name='登録日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'School'