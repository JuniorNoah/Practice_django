from django.db import models
from user.models import UserModel

class TextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    text = models.TextField()
    view_count = models.PositiveIntegerField()
    date = models.DateTimeField()
    author_id = models.ForeignKey(UserModel, related_name="author", on_delete=models.CASCADE, db_column="author_id")
    
    class Meta :
        db_table = "Text"
        ordering = ["title", "text", "view_count", "date", "author_id"]