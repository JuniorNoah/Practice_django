from django.db import models

class SelectSexModel(models.Model) :
    id = models.AutoField(primary_key=True)
    select_sex = models.CharField(max_length=30)