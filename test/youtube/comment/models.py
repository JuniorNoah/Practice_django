from django.db import models
from django.db.models.fields.related import ForeignKey
from user.models import UserModel
from django.db.models.fields import DateTimeField
from text.models import TextModel

class CommentModel(models.Model) :
    id = models.AutoField(primary_key=True)
    comment_author_id = models.ForeignKey(UserModel, related_name='comment_author', on_delete=models.CASCADE, db_column='comment_author_id')
    comment_contents = models.TextField()
    comment_date = DateTimeField(auto_now_add=True)
    text_field_id = ForeignKey(TextModel, related_name='text', on_delete=models.CASCADE, db_column='text_field_id')