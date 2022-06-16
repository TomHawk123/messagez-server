from django.db import models


class Post(models.Model):
    author = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    created_on = models.DateField(auto_now=True)
    body = models.TextField()
    tags = models.ManyToManyField(
        'ZASUser',
        through='AtTag',
        related_name='posts'
    )

    @property
    def tagged(self):
        """creates "tagged" property for Post objects that have tagged users on them"""
        return self.__tagged

    @tagged.setter
    def tagged(self, value):
        self.__tagged = value
