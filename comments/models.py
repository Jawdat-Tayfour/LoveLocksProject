from django.db import models
from django.contrib.auth import get_user_model


from padlocks.models import PadLock


class Comment(models.Model):
    post = models.ForeignKey(PadLock,related_name="comments",on_delete=models.CASCADE)
    creator = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=250)
    def __str__(self) -> str:
        return  "%s - %s" % (self.post.motto_field,self.creator.username)
    