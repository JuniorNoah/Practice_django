# Generated by Django 4.0 on 2022-01-05 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('black', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklist',
            name='black_user_id',
            field=models.ForeignKey(db_column='black_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='black_user', to='user.usermodel'),
        ),
    ]
