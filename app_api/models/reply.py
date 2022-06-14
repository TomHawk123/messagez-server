from django.db import models


class Reply(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    respondent = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_on = models.DateField(auto_now=True)
