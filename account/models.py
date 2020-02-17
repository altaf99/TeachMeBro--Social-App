from django.contrib import auth
from django.db import models
from django.db.models.deletion import CASCADE

class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)

class Post(models.Model):
    pic = models.ImageField(upload_to="images/",null=True, blank=True)
    subject = models.TextField(max_length=200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    upload_by = models.ForeignKey(to=User, on_delete= CASCADE,null=True, blank=True)
    
    def __str__(self):
        return "%s" % (self.subject)