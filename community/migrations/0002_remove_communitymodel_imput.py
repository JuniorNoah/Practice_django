# Generated by Django 4.0.1 on 2022-01-11 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitymodel',
            name='imput',
        ),
    ]