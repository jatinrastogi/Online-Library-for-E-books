from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .validators import validate_file_extension
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    book_writer = models.CharField(max_length=100,null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.FileField(upload_to="uploads/",null=True,validators=[validate_file_extension])
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_posted=date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s-%s' % (self.post.title,self.name)