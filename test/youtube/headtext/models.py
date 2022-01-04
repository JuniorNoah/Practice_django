from django.db import models

class HeadTextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    head = models.CharField(max_length=30)