# Generated by Django 3.2.8 on 2021-11-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSite', '0002_auto_20211102_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Admin',
            field=models.BooleanField(default=False, verbose_name='Is Admin'),
        ),
    ]