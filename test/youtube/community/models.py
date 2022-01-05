import re
from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from testapp.models import UserModel

class BlackList(models.Model) :
    id = models.AutoField(primary_key=True)
    black_user_id = models.ForeignKey(UserModel, related_name='black_user', on_delete=CASCADE, db_column='black_user_id')

class CommunityModel(models.Model) :
    id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(UserModel, related_name='admin', on_delete=CASCADE, db_column='admin_id')
    blaklist = 
    