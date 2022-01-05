# Generated by Django 4.0 on 2022-01-03 09:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique key', primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='User E-mail', max_length=254)),
                ('name', models.CharField(help_text='User Full Name', max_length=255)),
                ('age', models.PositiveIntegerField(help_text='User Age')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Created Date time')),
                ('update_date', models.DateTimeField(auto_now=True, help_text='Updated Date time')),
            ],
            options={
                'verbose_name': '유저 정보',
                'verbose_name_plural': '유저 정보',
                'ordering': ['name', 'age'],
            },
        ),
    ]