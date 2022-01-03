from django.db import models

class SubTextModel(models.Model) :
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=16)