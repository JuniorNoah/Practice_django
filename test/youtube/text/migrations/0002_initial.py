# Generated by Django 4.0 on 2022-01-05 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmodel',
            name='text_author_id',
            field=models.ForeignKey(db_column='text_author_id', on_delete=django.db.models.deletion.CASCADE, related_name='text_author', to='user.usermodel'),
        ),
    ]
