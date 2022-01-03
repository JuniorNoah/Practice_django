from django.db import models
from django.db.models.fields import DateTimeField
from subtext.models import SubTextModel as st_model

class TextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    text = models.TextField()
    view_count = models.PositiveIntegerField()
    date = DateTimeField()
    
    class Meta :
        db_table = "Text"
        ordering = ["title", "text", "view_count", "date"]