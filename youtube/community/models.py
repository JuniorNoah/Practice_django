from django.db import models
from user.models import UserModel
from black.models import BlackList

class CommunityModel(models.Model) :
    id = models.AutoField(primary_key=True)
    comm_admin_id = models.ForeignKey(UserModel, related_name='admin', on_delete=models.CASCADE, db_column='admin_id')
    blaklist = models.ForeignKey(BlackList, related_name='blacklist', on_delete=models.SET_NULL, null=True, db_column='black_list')
    