import uuid
from django.db import models

class UserModel(models.Model) :
    id = models.UUIDField(help_text='Unique key', primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(help_text='User E-mail')
    name = models.CharField(help_text='User Full Name', max_length=255)
    age = models.PositiveIntegerField(help_text='User Age')
    create_date = models.DateTimeField(help_text='Created Date time', auto_now_add=True)
    update_date = models.DateTimeField(help_text='Updated Date time', auto_now=True)
    
    class Meta :
        verbose_name = "유저 정보"
        verbose_name_plural = '유저 정보'
        ordering = ['name', 'age']