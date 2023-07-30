from django.shortcuts import render,redirect
from .models import LockRequest 
from users.models import CustomUser



def decline_request(request,id):
    lock_request = LockRequest.objects.get(id=id)
    LockRequest.objects.filter(id=id).delete()
    return redirect('home')

def accept_request(request,id):
    lock_request = LockRequest.objects.get(id=id)
    user1 = request.user
    user2 = lock_request.user1
    user1.user_is_reciever = True
    user2.user_is_sender = True
    user2.user_locked_with= str(user1.username)
    user1.user_locked_with= str(user2.username)
    user1.lock_status = True
    user2.lock_status = True 
    user1.lock_count -= 1 
    user2.lock_count -= 1 
    LockRequest.objects.filter(id=id).delete()
    user1.save()
    user2.save()    
    return redirect('home')
