from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000,blank=False,default=" Default Title")
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)

    content_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f'{self.user} posted at {self.content_at}'
    

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name= 'replies',on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    parent = models.ForeignKey('self',related_name='child_replies', on_delete=models.CASCADE, null = True, blank = True)
    image = models.ImageField(blank=True, null=True)

    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    commented_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        if self.parent:
            return f'Reply by {self.user.username} to {self.parent.user.username} on "{self.post.title}"'
        return f'Reply by {self.user.username} on "{self.post.title}"'

