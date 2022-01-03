from django.db import models

class MainPage(models.Model) :
    id = models.AutoField(primary_key=True)
    selection = models.PositiveSmallIntegerField()
    
    class Meta :
        db_table = "MainPage"
        ordering = ["id", "selection"]