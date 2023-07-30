from django.db import models
from users.models import CustomUser



class LockRequest(models.Model):
    user1 = models.OneToOneField(CustomUser,related_name="user1",on_delete=models.CASCADE)
    user2=models.OneToOneField(CustomUser,related_name="user2",on_delete=models.CASCADE)  
    

    

