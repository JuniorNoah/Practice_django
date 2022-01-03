from django.db import models

class UserModel(models.Model) :
    id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=16)
    login_pw = models.CharField(max_length=32)
    email = models.EmailField()
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=10)
    nickname = models.CharField(max_length=32)
    
    class Meta :
        db_table = "User"
        ordering = ["id", "login_id", "login_pw", "email", "name", "sex", "nickname"]