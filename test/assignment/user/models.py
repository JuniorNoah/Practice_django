from django.db import models

class UserModel(models.Model) :
    id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=30)
    login_pw = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    sex_selection = ('male', 'female')