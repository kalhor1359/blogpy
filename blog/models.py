from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensios = ['.jpg','.png']
    if not ext.lower() in valid_extensios:
        raise ValidationError('unsupported file extension')



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar', null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name
class Article(models.Model):
    objects = None
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)



class Category(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False)

    def __str__(self):
        return self.title


