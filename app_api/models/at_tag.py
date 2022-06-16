from django.db import models


class AtTag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tagged_user = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
