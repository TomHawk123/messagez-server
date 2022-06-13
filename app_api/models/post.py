from django.db import models


class Post(models.Model):
    author = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    created_on = models.DateField(auto_now=True)
    body = models.TextField()
    tags = models.ManyToManyField(
        'ZASUser',
        through='postTag',
        related_name='posts'
    )
