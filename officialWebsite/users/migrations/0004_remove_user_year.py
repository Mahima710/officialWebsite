# Generated by Django 4.0.2 on 2022-04-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220423_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='year',
        ),
    ]