from django.db import models
from user.models import UserModel

class BlackList(models.Model) :
    id = models.AutoField(primary_key=True)
    black_user_id = models.ForeignKey(UserModel, related_name='black_user', on_delete=models.CASCADE, db_column='black_user_id')