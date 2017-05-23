# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=128, verbose_name='\u5bc6\u7801')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('telephone', models.CharField(max_length=11, verbose_name='\u7528\u6237\u624b\u673a\u53f7\u7801')),
                ('gender', models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, verbose_name='\u6027\u522b')),
                ('birthday', models.DateField(verbose_name='\u51fa\u751f\u65e5\u671f')),
                ('avatar', models.ImageField(upload_to='./user/avatar/%Y/%m/%d')),
                ('presentation', models.CharField(max_length=100, verbose_name='\u4e00\u53e5\u8bdd\u4ecb\u7ecd\u81ea\u5df1')),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5728Admin\u4e2d\u53ef\u7528')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'ggsuer',
            },
        ),
        migrations.CreateModel(
            name='EducationExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50, verbose_name='\u5b66\u6821\u540d\u79f0')),
                ('major', models.CharField(max_length=50, verbose_name='\u4e3b\u4fee\u4e13\u4e1a')),
                ('start_time', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('gguser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'educationexperience',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('position', models.CharField(max_length=50, verbose_name='\u804c\u4f4d')),
                ('start_time', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('gguser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'workexperience',
            },
        ),
    ]