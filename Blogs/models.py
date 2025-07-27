from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_Title=models.CharField(max_length=100)
    blog_Description=models.CharField(max_length=500)

    def __str__(self):
        return self.blog_Title
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    comment=models.TextField()

    def __str__(self):
        return self.comment
