from django.db import models

class LoginModel(models.Model) :
    input_id = models.CharField(max_length=30)
    input_pw = models.CharField(max_length=100)