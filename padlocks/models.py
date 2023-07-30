from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MinLengthValidator



story = "Story"
motto = "Motto"
lock_natures =[(story,'Story'),(motto,'Motto')]
class PadLock(models.Model):
    start_date =  models.DateField()
    lock_nature = models.TextField(max_length=5,choices=lock_natures,default=story,null=True)
    motto_field = models.CharField(max_length=200)    
    story_field = models.TextField(max_length=20000,blank=True ,validators=[MinLengthValidator(4000)])
    active_state= models.BooleanField(default=False)
    creator = models.OneToOneField(get_user_model(),related_name="creator",on_delete=models.CASCADE,null=True)
    modifier = models.OneToOneField(get_user_model(),related_name="modifier",on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse("padlock_detail", args=[str(self.id)])
