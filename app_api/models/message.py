from django.db import models

class Message(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    sender = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    recipient = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
