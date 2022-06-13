from django.db import models

class Message(models.Model):
    sender = models.ForeignKey("ZASUser", on_delete=models.CASCADE, related_name='author')
    content = models.CharField(max_length=1000)
    recipient = models.ForeignKey("ZASUser", on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
