from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField("categoryName", max_length=20)
    category_description = models.TextField("categoryDescription", max_length=244)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_title = models.CharField("postTitle", max_length=30,blank=False)
    post_content = models.TextField("postContent",blank=False,null=False)
    post_created_datetime = models.DateTimeField("postCreateDate",auto_now_add=True)
    post_updated_date = models.DateTimeField("postUpdateDate",auto_now=True)
    post_category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,on_delete= models.CASCADE)
    comment_text = models.TextField("commentContent",blank=False,null=True)
    comment_created_datetime = models.DateTimeField("commentDateTime", auto_now_add=True)
    comment_updated_datetime = models.DateTimeField("commentUpdated", auto_now=True)

# class 

