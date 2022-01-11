from django.db import models

class UserModel(models.Model) :
    SEX = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=30, unique=True)
    login_pw = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    sex_selection = models.CharField(max_length=30, choices=SEX, default='Male')
    connection = models.BooleanField(default='False')