from django.db import models
from user.models import UserModel

class CommunityModel(models.Model) :
    id = models.AutoField(primary_key=True)
    community_admin_id = models.PositiveIntegerField()
    imput = models.PositiveIntegerField()
    
class PostModel(models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    post_contents = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_community_id = models.ForeignKey(CommunityModel, related_name="post_community", on_delete=models.CASCADE, db_column="post_community_id")
    post_author_id = models.ForeignKey(UserModel, related_name="post_author", on_delete=models.SET_NULL, null=True, db_column="text_author_id")
    view_count = models.PositiveIntegerField()
    
class HeadModel(models.Model) :
    id = models.AutoField(primary_key=True)
    head_community_id = models.ForeignKey(CommunityModel, related_name='head_community', on_delete=models.CASCADE, db_column='head_community_id')
    head_post_id = models.ForeignKey(PostModel, related_name='head_post', on_delete=models.CASCADE, db_column='head_post_id')
    head = models.CharField(max_length=30)

    
class CommentModel(models.Model) :
    id = models.AutoField(primary_key=True)
    comment_post_id = models.ForeignKey(PostModel, related_name='comment_post', on_delete=models.CASCADE, db_column='comment_post_id')
    comment_author_id = models.ForeignKey(UserModel, related_name='comment_author', on_delete=models.CASCADE, db_column='comment_author_id')
    comment_contents = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    