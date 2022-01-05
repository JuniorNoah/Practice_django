from django.db import models
from django.db.models.fields import DateTimeField, PositiveIntegerField
from user.models import UserModel
from headtext.models import HeadTextModel
from community.models import CommunityModel

class TextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    text_contents = models.TextField()
    view_count = PositiveIntegerField()
    text_date = DateTimeField(auto_now_add=True)
    text_author_id = models.ForeignKey(UserModel, related_name="text_author", on_delete=models.CASCADE, db_column="text_author_id")
    head_id = models.ForeignKey(HeadTextModel, related_name='text_head', on_delete=models.SET_DEFAULT, default=1, db_column='head_id')
    comm_id = models.ForeignKey(CommunityModel, related_name='community', on_delete=models.CASCADE, db_column='comm_id')