from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )