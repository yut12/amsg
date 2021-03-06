# Generated by Django 2.2.2 on 2022-01-10 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_task_task_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_name', models.CharField(max_length=20, verbose_name='問題名')),
                ('q_statement', models.CharField(max_length=200, verbose_name='問題文')),
                ('q_answer', models.CharField(max_length=200, verbose_name='問題文')),
                ('q_point', models.IntegerField(verbose_name='配点')),
                ('q_subject', models.CharField(max_length=20, verbose_name='教科')),
                ('q_unit', models.CharField(max_length=20, verbose_name='単元')),
                ('q_difficulty', models.IntegerField(verbose_name='難易度')),
                ('q_status', models.CharField(choices=[('0', '非公開'), ('1', '公開')], default='0', max_length=1, verbose_name='状態')),
                ('q_autostatus', models.CharField(choices=[('0', 'off'), ('1', 'on')], default='1', max_length=1, verbose_name='自動採点')),
                ('q_create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('q_update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('q_created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('q_school', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='accounts.School', verbose_name='学校')),
                ('q_task', models.ManyToManyField(to='task.Task')),
            ],
            options={
                'verbose_name_plural': 'Question',
            },
        ),
    ]
