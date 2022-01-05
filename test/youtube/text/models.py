from django.db import DefaultConnectionProxy, models
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import DateTimeField, PositiveIntegerField
from testapp.models import UserModel
from headtext.models import HeadTextModel
from community.models import CommunityModel

class TextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = PositiveIntegerField()
    date = DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(UserModel, related_name="author", on_delete=models.CASCADE, db_column="author_id")
    head_id = models.ForeignKey(HeadTextModel, related_name='head', on_delete=SET_DEFAULT, default=1, db_column='head_id')
    comm_id = models.ForeignKey(CommunityModel, related_name='community', on_delete=CASCADE, db_column='comm_id')