from django.db import models
from user.models import UserModel
from community.models import CommunityModel

class Blacklist(models.Model) :
    id = models.AutoField(primary_key=True)
    comm_id = models.ForeignKey(CommunityModel, related_name='block', on_delete=models.CASCADE, db_column='comm_id')
    blocked_id = models.ForeignKey(UserModel, related_name='blk_id', on_delete=models.CASCADE, db_column='blocked_id')
    
    def __str__(self) :
        return f'{self.comm_id} {self.blocked_id}'